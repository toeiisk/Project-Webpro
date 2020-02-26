from django.urls import path
from . import views
from dashboard.views import dashboard, edit, add

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/edit', edit, name='edit'),
    path('dashboard/add', edit, name='add'),
]