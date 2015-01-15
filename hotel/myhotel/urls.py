from django.conf.urls import url, patterns
import views


urlpatterns = patterns('',
                    url(r'^$', views.index, name='index'),
                    url(r'^registration/$', views.registration, name='registration'),
                    url(r'^profile/$', views.profile, name='profile'),
                    url(r'^welcome/(?P<userid>\d+)/$', views.welcome, name='welcome'),
                    url(r'^login/$', views.loginUser, name="login"),
                    url(r'^logout/$', views.logoutUser, name="logout"),
                    )
