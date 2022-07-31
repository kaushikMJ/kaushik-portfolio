from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from achievement import views

app_name='achievement'

urlpatterns = [
    
    #home page ie "/blog/"
    path('',views.achievement,name='achievements'),
    
]