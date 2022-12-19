from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CrossViewSet, MmrViewSet

router_v1 = DefaultRouter()

router_v1.register("cross", CrossViewSet, basename="cross")
router_v1.register("mmr", MmrViewSet, basename="mmr")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
