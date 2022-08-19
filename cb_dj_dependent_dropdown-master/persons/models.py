
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Consultant(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    place = models.CharField(max_length=200,default=False)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=124)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name