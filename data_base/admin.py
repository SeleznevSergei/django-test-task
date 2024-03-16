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

class CountryResource(resources.ModelResource):

    class Meta:
        model = Country
        fields = ['name']

class ManufacturerResource(resources.ModelResource):

    class Meta:
        model = Manufacturer
        fields = ['name', 'country__name']

class CommentResource(resources.ModelResource):

    class Meta:
        model = Comment
        fields = ['e_mail', 'car__name', 'time_created', 'time_updated', 'comment']


