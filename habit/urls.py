from django.urls import path

from .views import HabitListView, HabitDetailView, HabitCreateView, LogCreateView

app_name = 'habit'

urlpatterns = [
    path('', HabitListView.as_view()),
    path('<int:pk>/', HabitDetailView.as_view(), name='habitdetail'),
    path('create', HabitCreateView.as_view(), name='habitcreate'),
    path('<int:pk>/logs/create', LogCreateView.as_view(), name='logcreate'),
]
