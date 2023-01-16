# Create your views here.
from datetime import datetime, timedelta

from cross.models import Cross, History, Mmr
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CrossSerializer, HistoryCountSerializer, MmrSerializer


class CrossViewSet(viewsets.ModelViewSet):
    """Возвращает список имеющихся кроссов"""

    queryset = Cross.objects.all()
    serializer_class = CrossSerializer


class MmrViewSet(viewsets.ModelViewSet):
    """Возвращает список MMR кроссов"""

    queryset = Mmr.objects.all()
    serializer_class = MmrSerializer


class HistoryAPIView(APIView):
    """Возвращает историю использования патчкордов"""

    def get(self, request):
        date = datetime.now() - timedelta(days=31)
        count_fulltime = {
            "SC-SC": History.objects.filter(name="SC-SC").count(),
            "SC-LC": History.objects.filter(name="SC-LC").count(),
            "LC-LC": History.objects.filter(name="LC-LC").count(),
            "LC-FC": History.objects.filter(name="LC-FC").count(),
            "FC-SC": History.objects.filter(name="FC-SC").count(),
            "FC-FC": History.objects.filter(name="FC-FC").count(),
        }
        count_month = {
            "SC-SC": History.objects.filter(name="SC-SC")
            .filter(date__gt=date)
            .count(),
            "SC-LC": History.objects.filter(name="SC-LC")
            .filter(date__gt=date)
            .count(),
            "LC-LC": History.objects.filter(name="LC-LC")
            .filter(date__gt=date)
            .count(),
            "LC-FC": History.objects.filter(name="LC-FC")
            .filter(date__gt=date)
            .count(),
            "FC-SC": History.objects.filter(name="FC-SC")
            .filter(date__gt=date)
            .count(),
            "FC-FC": History.objects.filter(name="FC-FC")
            .filter(date__gt=date)
            .count(),
        }

        ser = {
            "count_fulltime": count_fulltime,
            "count_month": count_month,
        }
        serializer = HistoryCountSerializer(ser)
        return Response(serializer.data)
