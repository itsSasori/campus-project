from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    phone_number = models.BigIntegerField(null=False)
    messages  =models.TextField(null=True)

    def __str__(self):
        return self.name
    
