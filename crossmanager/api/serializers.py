from cross.models import Cross, Mmr
from rest_framework import serializers


class CrossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cross
        fields = "__all__"


class MmrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mmr
        fields = "__all__"
