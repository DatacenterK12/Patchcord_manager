from datetime import datetime, timedelta

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


class HistoryCountSerializer(serializers.Serializer):
    count_fulltime = serializers.JSONField()
    count_month = serializers.JSONField()
    result = serializers.SerializerMethodField()

    def get_result(self, obj):
        date = datetime.now() - timedelta(days=31)
        result = HistorySerializer(
            History.objects.filter(date__gt=date),
            many=True,
            read_only=True,
        )
        return result.data
