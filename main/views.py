from django.shortcuts import render
from .forms import RecordForm
from .models import Record
from datetime import datetime
from django.http import HttpResponseRedirect


def index(request):
    records = Record.objects.order_by("-created_date")
    return render(request, "index.html", {"records": records})


def record_new(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.author = request.user
            record.created_date = datetime.now()
            record.save()
            return HttpResponseRedirect("/")
    else:
        form = RecordForm()
    return render(request, "new_record.html", {"form": form})
