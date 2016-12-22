from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Record
from datetime import datetime


def index(request):
    records = Record.objects.order_by("-created_date")
    return render(request, "index.html", {"records": records})


def create_record_page(request):
    return render(request, "create_record.html")


def create_record(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        if (title != "" and text != ""):
            record = Record.create(request.user, title, text, datetime.now())
            record.save()
            return HttpResponseRedirect("/")

    return render(request, "create_record.html")
