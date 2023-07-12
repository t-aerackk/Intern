from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    message=models.TextField()
    