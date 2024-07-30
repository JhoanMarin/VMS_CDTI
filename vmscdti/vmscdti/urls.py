from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('cameras/', include('cameras.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    
]