from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('events/', views.event_list, name='event_list'),
]
