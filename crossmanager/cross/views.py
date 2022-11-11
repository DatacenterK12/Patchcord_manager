from django.shortcuts import get_object_or_404, render
from flexa import send_mail

from .models import Cross


# Create your views here.
def index(request):
    cross_data = Cross.objects.all()
    context = {
        "cross_data": cross_data,
    }
    return render(request, "cross/index.html", context)


def take_cross(request, name, length):
    cross = get_object_or_404(Cross, name=name)
    if length == "ten":
        cross.ten = cross.ten - 1
        length = 10
        if cross.ten <= 5:
            send_mail(name, length)
    elif length == "fifteen":
        cross.fifteen = cross.fifteen - 1
        length = 15
        if cross.fifteen <= 5:
            send_mail(name, length)
    elif length == "twenty":
        cross.twenty = cross.twenty - 1
        length = 20
        if cross.twenty <= 5:
            send_mail(name, length)
    elif length == "twentyfive":
        cross.twentyfive = cross.twentyfive - 1
        length = 25
        if cross.twentyfive <= 5:
            send_mail(name, length)
    elif length == "thirty":
        cross.thirty = cross.thirty - 1
        length = 30
        if cross.thirty <= 5:
            send_mail(name, length)
    elif length == "thirtyfive":
        cross.thirtyfive = cross.thirtyfive - 1
        length = 35
        if cross.thirtyfive <= 5:
            send_mail(name, length)
    cross.save()
    context = {
        "name": name,
        "cross": cross,
        "len": length,
    }
    return render(request, "cross/take_cross.html", context)
