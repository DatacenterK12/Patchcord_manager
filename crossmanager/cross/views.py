from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Cross, Mmr, New_stat, Statistic

DATA_PAGINATOR = 10


def paginator(request, pages, data_list):
    paginator = Paginator(data_list, pages)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    cross_data = Cross.objects.all()
    mmr_data = Mmr.objects.all()
    context = {
        "cross_data": cross_data,
        "mmr_data": mmr_data,
    }
    return render(request, "cross/index.html", context)


def statistic(request):
    stat_data = Statistic.objects.all()
    new_stat_data = New_stat.objects.all()
    context = {
        "stat_data": stat_data,
        "new_stat_data": paginator(request, DATA_PAGINATOR, new_stat_data),
    }
    return render(request, "cross/statistic.html", context)


def take_cross(request, name, length):
    if name != "MMR":
        cross = get_object_or_404(Cross, name=name)
        stat = get_object_or_404(Statistic, name=name)
    else:
        cross = get_object_or_404(Mmr, name=name)

    if length == "ten":
        cross.ten -= 1
        stat.ten += 1
        length = 10

    elif length == "fifteen":
        cross.fifteen -= 1
        stat.fifteen += 1
        length = 15

    elif length == "twenty":
        cross.twenty -= 1
        stat.twenty += 1
        length = 20

    elif length == "twentyfive":
        cross.twentyfive -= 1
        stat.twentyfive += 1
        length = 25

    elif length == "thirty":
        cross.thirty -= 1
        stat.thirty += 1
        length = 30

    elif length == "thirtyfive":
        cross.thirtyfive -= 1
        stat.thirtyfive += 1
        length = 35

    elif length == "one":
        cross.one -= 1
        length = 1

    elif length == "two":
        cross.two -= 1
        length = 2

    elif length == "three":
        cross.three -= 1
        length = 3

    elif length == "five":
        cross.five -= 1
        length = 5

    New_stat.objects.create(name=name, length=length)
    cross.save()
    if name != "MMR":
        stat.save()
    context = {
        "name": name,
        "cross": cross,
        "len": length,
    }
    return render(request, "cross/take_cross.html", context)
