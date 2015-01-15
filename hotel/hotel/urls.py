from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hotel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^myhotel/', include('myhotel.urls', namespace='myhotel')),
    url(r'', include('myhotel.urls', namespace='myhotel')),
)
