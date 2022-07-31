from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from experience import views

app_name='experience'

urlpatterns = [
    
    #home page ie "/blog/"
    path('',views.experience,name='experiences'),
    
]