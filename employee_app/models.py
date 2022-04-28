from django.db import models

# Create your models here.
class emp_info(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    designation=models.CharField(max_length=15)
    