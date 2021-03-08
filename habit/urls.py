from django.urls import path

from . import views

app_name = 'habit'

urlpatterns = [
    path('', views.HabitListView.as_view()),
    path('create/', views.HabitCreateView.as_view(), name='habitcreate'),
    path('<int:pk>/', views.HabitDetailView.as_view(), name='habitdetail'),
    path('<int:pk>/logs/create/', views.LogCreateView.as_view(),
         name='logcreate')
]
