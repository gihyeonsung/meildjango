from django import forms

from .models import Habit, Log


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'description', 'duration', 'count']


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['memo', 'habit']
