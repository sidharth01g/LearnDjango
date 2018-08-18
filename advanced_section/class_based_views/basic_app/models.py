from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=500)
    principal = models.CharField(max_length=500)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Get URL from view/model

        Returns:
            URL
        """
        return reverse(viewname='basic_app:school_create', kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    # related_name='students' allows us to use {% for student in school_detail.students.all %}
    # in school_detail.html
    school = models.ForeignKey(to=School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
