from django.shortcuts import render, get_object_or_404
from .forms import RecordForm
from .models import Record
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse


def cut_text(records):
    for record in records:
        if len(record.text) > 300:
            record.text = record.text[:300] + "...<a href='/record/" + str(record.id) + "'>Читать далее</a>"
    return records


def index(request):
    records = Record.objects.order_by("-created_date")
    records = cut_text(records)
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


def one_record(request, record_id):
    if request.method == "GET":
        record = get_object_or_404(Record, pk=record_id)
        return render(request, "one_record.html", {'record': record})
    elif request.method == "DELETE":
        Record.objects.get(pk=record_id).delete()
        return HttpResponse("ok")



def user_records(request, user_id):
    records = Record.objects.all().filter(author_id=user_id).order_by("-created_date")
    records = cut_text(records)
    return render(request, "user_records.html", {"records": records})

def search_records(request):
    search_text = request.POST.get("search_text", "")
    if search_text == "":
        return HttpResponseRedirect("/")
    records = Record.objects.all().filter(text__icontains=search_text).order_by("-created_date")
    records = cut_text(records)
    return render(request, "index.html", {"records": records, "search_text": search_text})

