from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('set_session_modal_add/', views.set_session_modal_add, name='set_session_modal_add'),
    path('remove_modal/', views.remove_modal, name='remove_modal'),
    path('new/',views.create_cameras, name='new')    
]
