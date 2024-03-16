from django.http import HttpResponse, HttpResponseNotFound
from import_export import resources
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .admin import CarResource, CountryResource, CommentResource, ManufacturerResource

from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer


# def export_data(request):
#     car_resource = CarResource()
#     data = car_resource.export()
#     param = request.GET.get('format')
#     response = HttpResponse(data.json, content_type='application/json')
#     if param == 'csv':
#         response = HttpResponse(data.csv, content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="data_base.csv"'
#     if param == 'xls':
#         response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
#         response['Content-Disposition'] = 'attachment; filename="data_base.xls"'
#     return response


def index(request):
    return HttpResponse("<h1>Home page</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")

class ExportMixinView(ModelViewSet):
    resource = resources.ModelResource

    def list(self, request, *args, **kwargs):
        param = request.GET.get('parametr', None)
        if param is not None:
            return self.get_file(param)
        return super(ExportMixinView, self).list(request, *args, **kwargs)

    def get_file(self, param):
        assert hasattr(self, 'resource'), f'Does not have class Resource in {self.resource.__class__.__name__}'
        data = self.resource.export()
        response = HttpResponse(data.json, content_type='application/json')
        if param == 'csv':
            response = HttpResponse(data.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data_base.csv"'
        if param == 'xls':
            response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="data_base.xls"'
        return response



#class CountryList(generics.ListCreateAPIView):
    #queryset = Country.objects.all()
    #serializer_class = CountrySerializer


#class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Country.objects.all()
    #serializer_class = CountrySerializer

class CountryModelViewSet(ExportMixinView, ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    resource = CountryResource()


#class ManufacturerList(generics.ListCreateAPIView):
    #queryset = Manufacturer.objects.all()
    #serializer_class = ManufacturerSerializer


#class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Manufacturer.objects.all()
    #serializer_class = ManufacturerSerializer

class ManufacturerModelViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


#class CarsList(generics.ListCreateAPIView):
    #queryset = Car.objects.all()
    #serializer_class = CarSerializer


#class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Car.objects.all()
    #serializer_class = CarSerializer

class CarModelViewSet(ExportMixinView, ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    resource = CarResource()


#class CommentList(generics.ListCreateAPIView):
    #queryset = Comment.objects.all()
    #serializer_class = CommentSerializer
    #permission_classes = (permissions.AllowAny,)


#class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Comment.objects.all()
    #serializer_class = CommentSerializer


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if not self.detail:
            permission_classes = (permissions.AllowAny,)
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]