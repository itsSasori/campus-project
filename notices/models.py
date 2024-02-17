from django.db import models

# Create your models here.
class Notices(models.Model):
    title = models.CharField(max_length=1024)
    images = models.ImageField(upload_to='notices', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    
class News(models.Model):
    topics = models.CharField(max_length=100)
    content = models.TextField(max_length=512)
    images = models.ImageField(upload_to='news', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.topics)

    
