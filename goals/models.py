from django.db import models

# Create your models here.
class goal(models.Model):
    typeof=models.CharField(max_length=300)
    descrip=models.TextField()
    who=models.CharField(max_length=200)
    