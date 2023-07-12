from django.contrib import admin
from .models import *


# Register your models here.
class PatientView(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','contact','address','message' ]
admin.site.register(Patient, PatientView)