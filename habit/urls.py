from django.urls import path

from .views import HabitListView, HabitDetailView, HabitCreateView

app_name = 'habit'

urlpatterns = [
    path('', HabitListView.as_view()),
    path('<int:pk>/', HabitDetailView.as_view(), name='habitdetail'),
    path('create', HabitCreateView.as_view())
]
