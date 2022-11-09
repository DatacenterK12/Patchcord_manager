from django.contrib import admin

from .models import Cross

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


admin.site.register(Cross, CrossAdmin)
