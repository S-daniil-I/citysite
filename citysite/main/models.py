from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=100, default="Без названия")
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='enterprise_photos/', blank=True, null=True)
    def __str__(self):
        return self.name

class SportObject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='sport_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    working_hours = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='service_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Leisure(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    address = models.CharField(max_length=300, blank=True)
    working_hours = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='leisure_photos/', blank=True, null=True)

    def __str__(self):
        return self.name