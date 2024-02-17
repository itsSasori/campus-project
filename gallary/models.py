from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Gallary(models.Model):
    name = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to='gallaries/thumbnail',null=True)

    def __str__(self):
        return self.name
    
class GallaryImage(models.Model):
    gallary = models.ForeignKey(Gallary, related_name="images",on_delete=models.CASCADE)
    pic = models.FileField(upload_to="gallaries/images")

    def __str__(self):
        return str(self.gallary.name) + " - " + str(self.pic)

class Downloads(models.Model):
    name =  models.CharField(max_length=50)
    file = models.FileField(upload_to='gallary/downloads',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class MainGallary(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='main_galleries/thumbnails')

    def __str__(self):
        return self.name
    

class MainGallaryImages(models.Model):
    main_gallary = models.ForeignKey(MainGallary, on_delete=models.CASCADE)
    pic = models.FileField(upload_to='main_galleries/pictures')


    def __str__(self):
        return str(self.main_gallary.name) + " - " + str(self.pic)
    
    
    