from django.urls import path, include
from .views import UserSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientview',UserSerializer, basename='clientview')

urlpatterns = [
    path('', include(router.urls))
]
