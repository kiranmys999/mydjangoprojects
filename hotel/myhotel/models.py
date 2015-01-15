from django.db import models

# Create your models here.
from xml.dom.minidom import parse
from django.contrib.auth.models import User


def countries():
    xmltree = parse('hotel/myhotel/country_data.xml')
    root = xmltree.documentElement
    objectlist = root.getElementsByTagName('object')
    countrylist = []
    for obj in objectlist:
        if obj.getElementsByTagName('field')[1].getAttribute('name') == u'printable_name':
            countryname = obj.getElementsByTagName('field')[1].childNodes[0].data
            countrylist.append((countryname, countryname))

    country_choices = tuple(countrylist)
    return country_choices

COUNTRY_CHOICES = countries()

CITIES = (
    ("Bangalore", "Bangalore"),
    ("Delhi", "Delhi"),
    ("Mumbai", "Mumbai"),
    ("Kolkata", "Kolkata"),
    ("Chennai", "Chennai"),
)


class RegisterUser(models.Model):
    user = models.OneToOneField(User)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    
    def __unicode__(self):
        return self.user.username


class Hotel(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=100, choices=CITIES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='hotelpics', blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


ROOM_TYPE = (
    ('Single', 'Single'),
    ('Double', 'Double'),
)

BOOKING_STATUS = (
    ('Booked', 'Booked'),
    ('Available', 'Available'),
)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel)
    type = models.CharField(max_length=10, choices=ROOM_TYPE, default='Double')
#    status = models.CharField(choices=BOOKING_STATUS)
    status = models.BooleanField(verbose_name='Booked?', default=False)
    rate = models.IntegerField(default=0)

    def __unicode__(self):
        return self.hotel.name


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel)
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    no_of_rooms = models.IntegerField(default=0)
