from django.contrib import admin

# Register your models here.
from persons.models import Consultant, Department, Appointment

admin.site.register(Consultant)
admin.site.register(Department)
admin.site.register(Appointment)