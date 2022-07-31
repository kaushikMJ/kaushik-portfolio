from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Experience


def experience(request):
    experiences = Experience.objects.order_by('-date')
    return render(request,"experiences.html",{'experiences':experiences})


