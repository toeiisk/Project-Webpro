from django.urls import path
from . import views
from details.views import details

urlpatterns = [
    path('details/', details, name='details'),
    path('logout/', views.auth_logout, name='logout'),
]