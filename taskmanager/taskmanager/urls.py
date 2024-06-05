from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('tasks/', include('taskmanaging.urls')),
    path('accounts/', include('accounts.urls')),
    path('logout/', views.logout_view, name='logout'),
    
]
