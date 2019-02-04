from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='annot-home'),
    path('annotation/',views.process, name='annot-process'),
    path('visualisation/', views.masonVisu, name='annot-visu')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)