from django.db import models

# Create your models here.

class Project(models.Model):
    # title = models.CharField(max_length=100)
    # description = models.CharField(max_length=600)
    # image = models.ImageField(upload_to='portfolio/images/')
    # url = models.URLField(blank=True)

    title = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=600,default='')
    longDescription = models.TextField(default='')
    startDate=models.DateField()
    endDate=models.DateField()
    techStack=models.TextField(default='')
    #image = models.ImageField(upload_to='portfolio/images/')
    imageurl= models.URLField(blank=True)
    githubUrl = models.URLField(blank=True)
    liveUrl=models.URLField(blank=True)




    #the below function actually shows the name of the objects as object's title instead of project(0),project(1),etc
    def __str__(self):
    	return self.title
        

