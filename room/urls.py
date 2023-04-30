from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('(?P<category_name_slug>[\w\-]+)/$/', views.room, name='room'),
    path('<int:pk>/', views.room, name='room'),
]