from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.exit, name='exit'),
    path('accounts/login/?next=/cameras/', views.login, name='login'),
    
]