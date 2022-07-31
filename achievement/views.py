from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Achievement


def achievement(request):
    achievements = Achievement.objects.all()
    return render(request,"achievements.html",{'achievements':achievements})