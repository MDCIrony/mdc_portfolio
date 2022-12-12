from django.db import models

# Create your models here.
class Projects(models.Model):

    title = models.CharField(max_length=200)

    type = models.CharField(max_length=100)

    date = models.DateField()

    technologies = models.TextField(max_length=400)

    def __str__(self):
        return self.title