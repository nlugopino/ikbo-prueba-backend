from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'ordenes', OrdenesViewSet, basename='ordenes')
router.register(r'tipo_ordenes', TipoOrdenViewSet, basename='tipo_ordenes')

urlpatterns = [
    path('', include(router.urls))
]
