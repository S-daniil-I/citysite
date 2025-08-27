from django.contrib import admin
from .models import Enterprise, SportObject, Leisure,Service,ServiceCategory

admin.site.register(Enterprise)
admin.site.register(SportObject)
admin.site.register(Leisure)
admin.site.register(Service)
admin.site.register(ServiceCategory)

# Register your models here.
