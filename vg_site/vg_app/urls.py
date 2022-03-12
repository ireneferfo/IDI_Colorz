from django.urls import path
from . import views

urlpatterns = [
    path('page', views.page, name='page'),
    path('', views.index, name='index'),
]