from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('events',views.events,name='events'),

    path('allteam/',views.allteam,name='allteam'),
   

    ]
#from django.conf.urls import url

#from . import views
#urlpatterns=[url(r'^events/$',views.events,name='events')]
