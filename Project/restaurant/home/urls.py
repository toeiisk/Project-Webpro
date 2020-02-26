from django.urls import path
from . import views 
from home.views import user_logout, success

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('success/', success, name='user_success'),
    path('logout/', user_logout, name='user_logout'),
]