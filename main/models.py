from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Record(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="None")
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    @classmethod
    def create(cls, author, title, text, date):
        record = cls(author=author, title=title, text=text, created_date=date)
        return record
