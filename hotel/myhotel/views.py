from django.shortcuts import render
from django.core.context_processors import request
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
#from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from forms import UserForm, RegisterUserForm, CityForm, HotelNameForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from models import Hotel
import pdb
import json
from django.core import serializers
from django import forms


def index(request):
    form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'myhotel/index.html', context)
    

def registration(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        reguser = RegisterUserForm(request.POST)

        if user.is_valid() and reguser.is_valid():
            userinst = user.save(commit=False)
            userinst.set_password(userinst.password)
            userinst.save()

            reguserinst = reguser.save(commit=False)
            reguserinst.user = userinst
            reguserinst.save()

            return HttpResponseRedirect(reverse('myhotel:welcome', args=(userinst.id,)))

        else:
            print user.errors, reguser.errors

    else:
        user = UserForm()
        reguser = RegisterUserForm()

    context = {'user': user, 'reguser': reguser, 'Cache-Control': 'no-cache'}
    return render(request, 'myhotel/registration.html', context)

def profile(request):
    user = request.POST['username']
    passwd = request.POST['password']
    lf = LoginForm(username=user, password=passwd)
    lf.save()
    #context = {'userid': lf.id}
    return HttpResponseRedirect(reverse('myhotel:welcome', args=(lf.id,)))
    #return HttpResponseRedirect(reverse('myhotel:welcome'))

@login_required
def welcome(request, userid):
    user = User.objects.get(pk=userid)
    #pdb.set_trace()
    print 'inside welcome view'
    if request.method == "POST":
        #pdb.set_trace()
        form = CityForm(request.POST)
        print 'form received'
        if form.is_valid():
            print 'form validated'
            cityname = form.cleaned_data['city']
            hotels = Hotel.objects.filter(city=cityname)
            hotelnames = [HotelNameForm.CHOICES[0]]
            for hotel in hotels:
                hotelnames.append((hotel.name, hotel.name))
            #print hotelnames
            formhotel = HotelNameForm()
            formhotel.fields['hotel_names'] = forms.ChoiceField(choices=tuple(hotelnames))
            #print formhotel.as_table()
            context = {'formhotel': formhotel.as_table()}
            #return HttpResponse('it worked!')
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            errormsg = form.errors
            context = {'error': errormsg}
            return render(request, 'myhotel/welcome.html', context)

    else:
        formcity = CityForm()
        formhotel = HotelNameForm()

    context = {'user': user, 'formcity': formcity, 'formhotel': formhotel}
    return render(request, 'myhotel/welcome.html', context)


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            #login(request, form.get_user())
            login(request, user)
            #return HttpResponseRedirect(reverse('myhotel:welcome', args=(form.get_user_id(),)))
            return HttpResponseRedirect(reverse('myhotel:welcome', args=(user.id,)))

    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'myhotel/login.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('myhotel:index'))