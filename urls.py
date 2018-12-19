from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),  #for the route that is posts/^$ start and end with nothing  go to view.index
    url(r'^details/(?P<id>\d+)/$', views.details, name='index')    #after details parameter id is a digit "+" more than one digit

];



