from django.contrib import admin
from django.urls import path 
from App import views
app_name='App'
urlpatterns = [
     
    path('', views.home,name='home'),
]