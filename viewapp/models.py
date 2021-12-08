from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} z {self.city} <{self.age}>"

