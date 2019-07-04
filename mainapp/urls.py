from django.urls import path

from . import views


urlpatterns = [
    path('', views.listview, name='list'),
    path('detail/<pk>/', views.detail, name='detail'),
]
