from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Главная", "content": "Магазин украшений N.V.E Jewerly"}

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Главная",
        "content": "Магазин украшений N.V.E Jewerly",
        "text_on_page": "Почему этот магазим",
    }

    return render(request, "main/about.html", context)
