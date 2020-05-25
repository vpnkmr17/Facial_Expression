
from django.urls import path, include
from . import views

app_name='Facial_Expression'

urlpatterns = [
    path('',views.home),
    path('webcam/',views.predict,name="webcam"),
]
