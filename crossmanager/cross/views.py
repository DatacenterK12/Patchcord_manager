from django.shortcuts import get_object_or_404, render

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
    elif length == "fifteen":
        cross.fifteen = cross.fifteen - 1
        length = 15
    elif length == "twenty":
        cross.twenty = cross.twenty - 1
        length = 20
    elif length == "twentyfive":
        cross.twentyfive = cross.twentyfive - 1
        length = 25
    elif length == "thirty":
        cross.thirty = cross.thirty - 1
        length = 30
    elif length == "thirtyfive":
        cross.thirtyfive = cross.thirtyfive - 1
        length = 35
    elif length == "one":
        cross.one = cross.one - 1
        length = 1
    elif length == "two":
        cross.two = cross.two - 1
        length = 2
    elif length == "three":
        cross.three = cross.three - 1
        length = 3
    elif length == "five":
        cross.five = cross.five - 1
        length = 5

    cross.save()
    context = {
        "name": name,
        "cross": cross,
        "len": length,
    }
    return render(request, "cross/take_cross.html", context)
