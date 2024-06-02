from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('dreams/', views.dream_index, name='dream-index'),
  path('dreams/<int:dream_id>/', views.dream_detail, name='dream-detail')
]