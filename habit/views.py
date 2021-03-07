from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Habit
from .forms import HabitForm


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
        context['object_list'] = object_list
        return context


class HabitCreateView(CreateView):
    model = Habit
    form_class = HabitForm
    success_url = '/'
