from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Habit
from .forms import HabitForm


class HabitListView(ListView):
    model = Habit


class HabitCreateView(CreateView):
    model = Habit
    form_class = HabitForm
    success_url = '/'
