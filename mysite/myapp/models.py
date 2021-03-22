from django.db import models

# Create your models here.
class Book(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()

class lavs(models.Model):

    def __str__(self):
        return self.series
    series = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)

# class Person(models.Model):

#     def __str__(self):
#        return self.first_name
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
    
    