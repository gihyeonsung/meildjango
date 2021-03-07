from django.db import models


class Log(models.Model):
    memo = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Habit(models.Model):
    title = models.CharField()
    description = models.TextField()
    duration = models.TimeField()
    count = models.IntegerField()
    logs = models.ForeignKey(Log, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
