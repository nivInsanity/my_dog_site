from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name} {self.race}"