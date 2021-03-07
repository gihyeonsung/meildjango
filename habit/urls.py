from django.urls import path

from .views import HabitListView, HabitCreateView

urlpatterns = [
    path('', HabitListView.as_view()),
    path('create', HabitCreateView.as_view())
]
