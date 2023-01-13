from cross.models import Cross, History, Mmr, Statistic
from rest_framework import serializers


class CrossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cross
        exclude = ("id",)
        read_only_fields = ("name",)


class MmrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mmr
        exclude = ("id",)
        read_only_fields = ("name",)


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        exclude = ("id",)


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        exclude = ("id",)
