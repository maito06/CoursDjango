from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('date', views.date_actuelle, name = 'date'),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition, name = 'addition'),
]
