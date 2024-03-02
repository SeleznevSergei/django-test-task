from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from rest_framework import serializers

from data_base.models import Comment, Car, Manufacturer, Country
import tablib

admin.site.register(Comment)
admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Country)

class CarResource(resources.ModelResource):

    class Meta:
        model = Car
        fields = ['name', 'manufacturer__name', 'manufacturer__country__name']


