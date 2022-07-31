"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('',views.home,name="home"),
    path('admin_kaushik_rina/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('portfolio/',include('portfolio.urls')),
    path('experience/',include('experience.urls')),
    path('achievement/',include('achievement.urls')),
    #path('codingProfile/',views.codingProfile,name="codingProfile"),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#https://drive.google.com/uc?export=view&id=1WrrwAn50_I_0lCV_AMxsZHMXiNerx6mB
#http://drive.google.com/uc?export=view&id=1yz6ZSUqSiP6bM0Uc-Wz3pb51nwWgn_4Y