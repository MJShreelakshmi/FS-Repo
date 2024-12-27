from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length = 100, primary_key=True)

class Capital(models.Model):
    capital = models.CharField(max_length=100)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)


