from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

app_name='portfolio'

urlpatterns = [
    
    #home page ie "/portfolio/"
    path('',views.allProjects,name='allProjects'),
    path('<int:projectId>/',views.detailProject,name='detailProject'),
    path('codingProfile/',views.codingProfile,name="codingProfile"),

]
