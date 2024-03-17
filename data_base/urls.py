from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'country', views.CountryModelViewSet)
router.register(r'manufacture', views.ManufacturerModelViewSet)
router.register(r'car', views.CarModelViewSet)
router.register(r'comment', views.CommentModelViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('api/v1/', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
