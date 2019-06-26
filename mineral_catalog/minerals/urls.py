from django.urls import path

from . import views

app_name = 'minerals'
urlpatterns = [
    path('', views.minerals_home, name='minerals-home'),
    path('<int:pk>', views.mineral_detail, name='minerals-detail'),
    path('random/', views.mineral_random, name='minerals-random'),
]