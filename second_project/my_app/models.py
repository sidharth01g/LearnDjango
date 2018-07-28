from django.db import models


# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __repr__(self):
        return self.topic_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __repr__(self):
        return self.name


class AccessRecord(models.Model):
    webpage = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __repr__(self):
        return str(self.date)