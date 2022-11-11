from django.urls import path

from . import views

app_name = "cross"

urlpatterns = [
    path("", views.index, name="index"),
    path("take/<str:name>/<str:length>/", views.take_cross, name="take_cross"),
]
