from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.rest_search, name='rest_search'),
    path('login/', views.auth_login, name='login'),
    path('logout/', views.auth_logout, name='logout'),
    path('filter/<int:faculty_id>/', views.rest_seemore, name='seemore')
]