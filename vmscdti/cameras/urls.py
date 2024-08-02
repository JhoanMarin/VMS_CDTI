from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.create_cameras, name='new'),
    path('modal_new/', views.modal_new, name='modal_new'),
    path('modal_remove/', views.modal_remove, name='modal_remove'),
    path('<int:cam>/', views.camera_detail, name='camera_detail'),
]
