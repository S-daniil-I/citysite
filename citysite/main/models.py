from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=100),
    description = models.TextField(blank=True),
    address = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return self.name

class SportObject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300, blank=True)
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

    def __str__(self):
        return self.name