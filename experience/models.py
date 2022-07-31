from django.db import models

# Create your models here.
class Experience(models.Model):
    companyName = models.CharField(max_length=200)
    date=models.CharField(max_length=30)
    designation=models.CharField(max_length=100)
    description = models.TextField()
    #image = models.ImageField(upload_to='portfolio/images/')
    


    #the below function actually shows the name of the objects as object's title instead of blog(0),blog(1),etc
    def __str__(self):
    	return self.companyName