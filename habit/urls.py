from django.urls import path

from . import views

app_name = 'habit'

urlpatterns = [
    path('', views.HabitListView.as_view(), name='habitlist'),
    path('create/', views.HabitCreateView.as_view(), name='habitcreate'),
    path('<int:pk>/', views.HabitDetailView.as_view(), name='habitdetail'),
    path('<int:pk>/delete', views.HabitDeleteView.as_view(),
         name='habitdelete'),
    path('<int:pk>/logs/create/', views.LogCreateView.as_view(),
         name='logcreate'),
    path('<int:habitpk>/logs/<int:pk>/', views.LogDetailView.as_view(),
         name='logdetail'),
    path('<int:habitpk>/logs/<int:pk>/delete/', views.LogDeleteView.as_view(),
         name='logdelete'),
]
