from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='annot-home'),
    path('about/', views.about, name='annot-about'),
]