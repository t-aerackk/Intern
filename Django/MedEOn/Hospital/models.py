from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    message=models.TextField()
    
    def __str__(self):
        return self.address
    

class Appointment(models.Model):
    appointment_type = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    signs_symptoms = models.TextField(blank=True)
    preferred_doctor = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.appointment_type} - {self.date} {self.time}"

    