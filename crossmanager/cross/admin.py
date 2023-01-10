from django.contrib import admin

from .models import Cross, Mmr, New_stat, Statistic

# Register your models here.


class CrossAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ten",
        "fifteen",
        "twenty",
        "twentyfive",
        "thirty",
        "thirtyfive",
    )
    search_fields = ("name",)
    empty_value_display = "-пусто-"


class MmrAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "one",
        "two",
        "three",
        "five",
    )
    search_fields = ("name",)
    empty_value_display = "-пусто-"


class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ten",
        "fifteen",
        "twenty",
        "twentyfive",
        "thirty",
        "thirtyfive",
    )
    search_fields = ("name",)
    empty_value_display = "-пусто-"


class NewStatAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "length",
        "date",
    )
    search_fields = (
        "name",
        "date",
    )
    empty_value_display = "-пусто-"


admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Cross, CrossAdmin)
admin.site.register(Mmr, MmrAdmin)
admin.site.register(New_stat, NewStatAdmin)
