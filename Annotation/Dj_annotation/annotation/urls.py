from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='annot-home'),
    path('annotation/',views.process, name='annot-process')
]
