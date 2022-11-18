from django.contrib import admin

from .models import Cross, Mmr

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
    )
    search_fields = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Cross, CrossAdmin)
admin.site.register(Mmr, MmrAdmin)
