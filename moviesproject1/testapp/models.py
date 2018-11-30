from django.db import models

# Create your models here.
class Jobs(models.Model):
    date=models.DateField()
    companyname=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField()
    phoneno=models.IntegerField()
