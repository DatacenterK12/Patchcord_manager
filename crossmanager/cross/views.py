from django.shortcuts import get_object_or_404, render
from flexa import send_mail

from .models import Cross, Mmr


# Create your views here.
def index(request):
    cross_data = Cross.objects.all()
    mmr_data = Mmr.objects.all()
    context = {
        "cross_data": cross_data,
        "mmr_data": mmr_data,
    }
    return render(request, "cross/index.html", context)


def take_cross(request, name, length):
    if name != "MMR":
        cross = get_object_or_404(Cross, name=name)
    else:
        cross = get_object_or_404(Mmr, name=name)

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
    elif length == "one":
        cross.one = cross.one - 1
        length = 1
        if cross.one <= 5:
            send_mail(name, length)
    elif length == "two":
        cross.two = cross.two - 1
        length = 2
        if cross.two <= 5:
            send_mail(name, length)
    elif length == "three":
        cross.three = cross.three - 1
        length = 3
        if cross.three <= 5:
            send_mail(name, length)
    elif length == "five":
        cross.five = cross.five - 1
        length = 5
        if cross.five <= 5:
            send_mail(name, length)

    cross.save()
    context = {
        "name": name,
        "cross": cross,
        "len": length,
    }
    return render(request, "cross/take_cross.html", context)
