from django.contrib import admin
from .models import *


# Register your models here.
class PatientView(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','contact','address','message' ]
admin.site.register(Patient, PatientView)

class AppointView(admin.ModelAdmin):
    list_display=['id','appointment_type', 'preferred_location','department','signs_symptoms','date', 'time', 'preferred_doctor']
admin.site.register(Appointment, AppointView)

# class BlogPost(admin.ModelAdmin):
#     list_display=['sno', 'title', 'content', 'author', 'slug', 'timestamp']
# admin.site.register(Post, BlogPost)

