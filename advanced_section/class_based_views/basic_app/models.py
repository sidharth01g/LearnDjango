from django.db import models


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=500)
    principal = models.CharField(max_length=500)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    school = models.ForeignKey(to=School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
