from django.urls import path     
from . import views    # le .   indique que le fichier de vues se trouve dans le même répertoire que ce fichier
urlpatterns = [
    path('', views.index),
    path('result', views.result),
]