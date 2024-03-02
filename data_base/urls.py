from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('api/v1/country/', views.CountryList.as_view()),
    path('api/v1/country/<int:pk>/', views.CountryDetail.as_view()),
    path('api/v1/manufacture/', views.ManufacturerList.as_view()),
    path('api/v1/manufacture/<int:pk>/', views.ManufacturerDetail.as_view()),
    path('api/v1/car/', views.CarsList.as_view()),
    path('api/v1/car/<int:pk>/', views.CarsDetail.as_view()),
    path('api/v1/comment/', views.CommentList.as_view()),
    path('api/v1/comment/<int:pk>/', views.CommentDetail.as_view()),
    path('export_data/', views.export_data),
]

urlpatterns = format_suffix_patterns(urlpatterns)
