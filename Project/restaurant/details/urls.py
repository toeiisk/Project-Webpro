from django.urls import path
from . import views
from details.views import details

urlpatterns = [
    path('details/', details, name='details'),
]