from django.db import models
from django.db import connection

# Create your models here.
class Contact2(models.Model):
    name2=models.CharField(max_length=122)