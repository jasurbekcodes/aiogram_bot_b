from django.urls import path
from .views import handle_update

urlpatterns = [
    path('webhook/', handle_update),
]
