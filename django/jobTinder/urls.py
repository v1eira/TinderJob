from django.urls import path
from .views import views

urlpatterns = [
    path('', views.candidatos_list, name='candidatos_list'),
]
