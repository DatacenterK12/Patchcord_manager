from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CrossViewSet, HistoryVeiwSet, MmrViewSet, StatisticViewSet

router_v1 = DefaultRouter()

router_v1.register("cross", CrossViewSet, basename="cross")
router_v1.register("mmr", MmrViewSet, basename="mmr")
router_v1.register("statistic", StatisticViewSet, basename="statistic")
router_v1.register("history", HistoryVeiwSet, basename="history")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
