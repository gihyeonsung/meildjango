from django import forms

from .models import Habit, Log


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'duration', 'count']
        labels = {
            'name': '만들 습관의 이름이 뭔가요?',
            'description': '어떤 습관인가요?',
            'duration': '얼마나 자주 반복하나요?',
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
