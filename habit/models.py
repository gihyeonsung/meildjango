from django.db import models
from django.urls import reverse
from django.utils import timezone


class Habit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    count = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('habit:habitdetail', args=[str(self.id)])

    def get_last_log(self):
        return Log.objects.order_by('created').first()

    def get_logs(self):
        return Log.objects.order_by('-created')

    def get_curr_start(self):
        curr_index = (timezone.now() - self.created) // self.duration
        return self.created + curr_index * self.duration

    def get_curr_end(self):
        return self.get_curr_start() + self.duration

    def get_curr_remaining(self):
        return self.get_curr_end() - timezone.now()

    def get_curr_logcount(self):
        return Log \
            .objects \
            .filter(created__gte=self.get_curr_start()) \
            .filter(created__lt=self.get_curr_end()) \
            .count()


class Log(models.Model):
    memo = models.TextField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
