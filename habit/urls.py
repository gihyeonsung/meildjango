from django.urls import path

from .views import HabitListView

urlpatterns = [
    path('', HabitListView.as_view())
]
