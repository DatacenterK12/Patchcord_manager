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
    count_fulltime = serializers.SerializerMethodField()
    count_month = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()

    def get_count_fulltime(self, obj):
        return {
            "SC-SC": History.objects.filter(name="SC-SC").count(),
            "SC-LC": History.objects.filter(name="SC-LC").count(),
            "LC-LC": History.objects.filter(name="LC-LC").count(),
            "LC-FC": History.objects.filter(name="LC-FC").count(),
            "FC-SC": History.objects.filter(name="FC-SC").count(),
            "FC-FC": History.objects.filter(name="FC-FC").count(),
        }

    def get_count_month(self, obj):
        date = datetime.now() - timedelta(days=31)
        return {
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

    def get_result(self, obj):
        date = datetime.now() - timedelta(days=31)
        result = HistorySerializer(
            History.objects.filter(date__gt=date),
            many=True,
            read_only=True,
        )
        return result.data
