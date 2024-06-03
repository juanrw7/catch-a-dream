from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('dreams/', views.dream_index, name='dream-index'),
  path('dreams/<int:dream_id>/', views.dream_detail, name='dream-detail'),
  path('dreams/create', views.DreamCreate.as_view(), name='dream-create'),
  path('dreams/<int:pk>/update/', views.DreamUpdate.as_view(), name='dream-update'),
  path('dreams/<int:pk>/delete/', views.DreamDelete.as_view(), name='dream-delete'),

  path('accounts/signup/', views.signup, name='signup'),
]