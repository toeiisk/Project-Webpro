from django.urls import path
from . import views
from dashboard.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', views.auth_logout, name='logout'),
]