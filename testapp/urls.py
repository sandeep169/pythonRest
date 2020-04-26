from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index),
    path('userdata',views.get_data,name='pythonRest_apiData')
]
