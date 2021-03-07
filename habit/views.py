from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Habit, Log
from .forms import HabitForm, LogForm


class HabitListView(ListView):
    model = Habit

    def create_object(self, habit: Habit):
        return {
            'title': habit.title,
            'count': habit.count,
            'session_remaining': habit.get_current_session_remaining(),
            'session_start': habit.get_current_session_start(),
            'session_end': habit.get_current_session_end(),
            'session_log_count': habit.get_current_session_log_count()
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = list(context['object_list'])
        object_list = map(self.create_object, object_list)
        object_list = sorted(object_list, key=lambda k: k['session_remaining'])
        context['object_list'] = object_list
        return context


class HabitDetailView(DetailView):
    model = Habit

    def create_object(self, habit: Habit):
        return {
            'title': habit.title,
            'description': habit.description,
            'count': habit.count,
            'session_remaining': habit.get_current_session_remaining(),
            'session_log_count': habit.get_current_session_log_count(),
            'logs': habit.get_logs()
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.create_object(context['object'])
        return context


class HabitCreateView(CreateView):
    model = Habit
    form_class = HabitForm


class LogCreateView(CreateView):
    model = Log
    form_class = LogForm
