from django.shortcuts import get_object_or_404, render

# Create your views here.

#import project model here
from .models import Project
def home(request):
    #grab all the project objects here
    #projects= Project.objects.all()[0].title
    projects= Project.objects.all()
    return render(request,'home.html',{'projects':projects})


def codingProfile(request):
    return render(request,'codingProfile.html')


def allProjects(request):
    projects= Project.objects.all()
    return render(request,'allProjects.html',{'projects':projects})


def detailProject(request,projectId):
    project=get_object_or_404(Project,pk=projectId)
    return render(request,'detailProject.html',{'project':project})
