from django import forms
from django.utils import timezone

from .models import Habit, Log


class DaysDurationField(forms.IntegerField):

    def to_python(self, value):
        days = super().to_python(value)
        return days * timezone.timedelta(days=1)


class HabitForm(forms.ModelForm):

    duration = DaysDurationField(label='몇일마다 반복하나요?', initial=1)

    class Meta:
        model = Habit
        fields = ['name', 'description', 'duration', 'count']
        labels = {
            'name': '만들 습관의 이름이 뭔가요?',
            'description': '어떤 습관인가요?',
            'count': '얼마나 많이 반복하나요?',
        }


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['memo', 'habit']
        labels = {
            'memo': '메모를 남겨주세요',
        }
        widgets = {
            'habit': forms.HiddenInput(),
        }
