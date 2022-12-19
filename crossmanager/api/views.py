# Create your views here.
from cross.models import Cross, Mmr
from rest_framework import viewsets

from .serializers import CrossSerializer, MmrSerializer


class CrossViewSet(viewsets.ModelViewSet):
    queryset = Cross.objects.all()
    serializer_class = CrossSerializer


class MmrViewSet(viewsets.ModelViewSet):
    queryset = Mmr.objects.all()
    serializer_class = MmrSerializer
