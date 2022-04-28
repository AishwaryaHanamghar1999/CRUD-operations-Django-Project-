from django.contrib import admin
from .models import emp_info

# Register your models here.

class empadmin(admin.ModelAdmin):
    list_display=['name','email','designation']
admin.site.register(emp_info,empadmin)