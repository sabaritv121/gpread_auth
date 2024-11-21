from django.db import models

# Create your models here.


class Enquiry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    email= models.EmailField()