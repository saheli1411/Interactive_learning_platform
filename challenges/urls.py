from django.urls import path
from .views import get_challenges

urlpatterns = [
    path('challenges/', get_challenges, name="get_challenges"),
]
