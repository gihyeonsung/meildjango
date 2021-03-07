from django.views.generic import ListView

from .models import Habit


class HabitListView(ListView):
    model = Habit
