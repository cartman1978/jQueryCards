from django.db import models
from django.conf import settings
# from django.core.files.storage import FileSystemStorage


class personal(models.Model):
    name = models.CharField(max_length=100)
    last_ame = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class company(models.Model):
    organization = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    vat = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.organization


class documentation(models.Model):
    poi = models.FileField(upload_to='media')
    pob = models.FileField(upload_to='media')

    def __str__(self):
        return self.poi
