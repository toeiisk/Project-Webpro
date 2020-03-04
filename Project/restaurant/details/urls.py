from django.urls import path
from . import views
from details.views import details

urlpatterns = [
    path('<int:rest_id>', details, name='details'),
]