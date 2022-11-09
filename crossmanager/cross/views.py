from django.shortcuts import get_object_or_404, render

from .models import Cross


# Create your views here.
def index(request):
    cross_data = Cross.objects.all()
    context = {
        "cross_data": cross_data,
    }
    return render(request, "cross/index.html", context)


def take_cross(request, name, len):
    cross = get_object_or_404(Cross, name=name)
    if len == "ten":
        cross.ten = cross.ten - 1
    elif len == "fifteen":
        cross.fifteen = cross.fifteen - 1
    elif len == "twenty":
        cross.twenty = cross.twenty - 1
    elif len == "twentyfive":
        cross.twentyfive = cross.twentyfive - 1
    elif len == "thirty":
        cross.thirty = cross.thirty - 1
    elif len == "thirtyfive":
        cross.thirtyfive = cross.thirtyfive - 1
    cross.save()
    context = {
        "name": name,
        "cross": cross,
        "len": len,
    }
    return render(request, "cross/take_cross.html", context)
