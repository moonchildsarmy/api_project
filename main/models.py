from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.title
# Create your models here.
