from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .admin import CarResource

from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer
import xlsxwriter
import xlwt


def export_data(request):
    car_resource = CarResource()
    data = car_resource.export()
    param = request.GET.get('format')
    response = HttpResponse(data.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="data_base.json"'
    if param == 'csv':
        response = HttpResponse(data.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data_base.csv"'
    if param == 'xls':
        response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="data_base.xls"'
    return response


def index(request):
    return HttpResponse("<h1>Home page</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarsList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
