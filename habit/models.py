from django.db import models
from django.urls import reverse
from django.utils import timezone


def truncate_datetime_days(datetime: timezone.datetime):
    return datetime.replace(hour=0, minute=0, second=0, microsecond=0)


class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.DurationField(default=timezone.timedelta(days=1))
    count = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('habit:habitdetail', args=[str(self.id)])

    def get_logs(self):
        return Log.objects.filter(habit=self.pk).order_by('-created')

    def get_curr_index(self):
        now = truncate_datetime_days(timezone.localtime())
        created = truncate_datetime_days(timezone.localtime(self.created))
        try:
            return (now - created) // self.duration
        except ZeroDivisionError:
            return created

    def get_curr_start(self):
        created = truncate_datetime_days(timezone.localtime(self.created))
        return created + (self.get_curr_index() * self.duration)

    def get_curr_end(self):
        return self.get_curr_start() + self.duration

    def get_curr_remaining(self):
        return self.get_curr_end() - truncate_datetime_days(
            timezone.localtime())

    def get_curr_count(self):
        return self.get_logs() \
            .filter(created__gte=self.get_curr_start()) \
            .filter(created__lt=self.get_curr_end()) \
            .count()


class Log(models.Model):
    memo = models.TextField(blank=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
