from django.db import models

# Create your models here.
class BoardMembers(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    location = models.TextField(default="")
    images = models.ImageField(upload_to='board/',blank=True,null=True)

    def __str__(self):
        return self.name
    

class AdvisoryMembers(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    location = models.TextField(default="")
    images = models.ImageField(upload_to='advisors/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class PatronMembers(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    location = models.TextField(default="")
    images = models.ImageField(upload_to='patrons/',blank=True,null=True)

    def __str__(self):
        return self.name
    


