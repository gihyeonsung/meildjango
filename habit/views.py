from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

from . import models, forms


class HabitListView(ListView):
    model = models.Habit

    def create_object(self, habit: models.Habit):
        return {
            'pk': habit.pk,
            'title': habit.title,
            'count': habit.count,
            'curr_remaining': habit.get_curr_remaining(),
            'curr_count': habit.get_curr_count(),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = context['object_list']
        object_list = map(self.create_object, object_list)
        object_list = sorted(object_list, key=lambda k: k['curr_remaining'])
        context['object_list'] = object_list
        return context


class HabitDetailView(DetailView):
    model = models.Habit

    def create_object(self, habit: models.Habit):
        return {
            'title': habit.title,
            'description': habit.description,
            'count': habit.count,
            'curr_remaining': habit.get_curr_remaining(),
            'curr_count': habit.get_curr_count(),
            'logs': habit.get_logs()
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.create_object(context['object'])
        return context


class HabitDeleteView(DeleteView):
    model = models.Habit

    def get_success_url(self):
        return reverse('habit:habitlist')


class HabitCreateView(CreateView):
    model = models.Habit
    form_class = forms.HabitForm


class LogCreateView(CreateView):
    model = models.Log
    form_class = forms.LogForm

    def get_success_url(self):
        return reverse('habit:habitdetail', args=[str(self.kwargs.get('pk'))])

    def get_initial(self):
        return {'habit': self.kwargs.get('pk')}


class LogDetailView(DetailView):
    model = models.Log


class LogDeleteView(DeleteView):
    model = models.Log

    def get_success_url(self):
        return reverse(
            'habit:habitdetail', args=[str(self.kwargs.get('habitpk'))])
