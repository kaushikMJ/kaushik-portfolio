from django.db import models

# Create your models here.
class Achievement(models.Model):
    description = models.TextField()
    date = models.CharField(max_length=30)
    url = models.URLField(blank=True)
    #image = models.ImageField(upload_to='portfolio/images/')
    


    #the below function actually shows the name of the objects as object's title instead of blog(0),blog(1),etc
    def __str__(self):
    	return self.description