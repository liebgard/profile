from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bssm_home'),
    path('about/', views.about, name='bssm_about'),
]
