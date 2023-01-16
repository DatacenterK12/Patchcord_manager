# Create your views here.
from cross.models import Cross, History, Mmr, Statistic
from rest_framework import viewsets

from .serializers import (
    CrossSerializer,
    HistoryCountSerializer,
    MmrSerializer,
    StatisticSerializer,
)


class CrossViewSet(viewsets.ModelViewSet):
    """Возвращает список имеющихся кроссов"""

    queryset = Cross.objects.all()
    serializer_class = CrossSerializer


class MmrViewSet(viewsets.ModelViewSet):
    """Возвращает список MMR кроссов"""

    queryset = Mmr.objects.all()
    serializer_class = MmrSerializer


class StatisticViewSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает общую статистику по кросам"""

    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class HistoryVeiwSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает историю использования патчкордов"""

    queryset = History.objects.filter(pk=1)
    serializer_class = HistoryCountSerializer
