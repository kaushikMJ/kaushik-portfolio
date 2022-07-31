from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    date = models.DateField(auto_now=True)


    #the below function actually shows the name of the objects as object's title instead of blog(0),blog(1),etc
    def __str__(self):
    	return self.title
        