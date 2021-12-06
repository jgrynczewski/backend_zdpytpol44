from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Capital(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# class Country(models.Model):
#     name = models.CharField(max_length=128)
#     capital = models.OneToOneField(Capital, on_delete=models.CASCADE)


class Language(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name