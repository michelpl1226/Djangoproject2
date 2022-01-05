from django.urls import path

from app.core.erp.views import first
from app.core.erp.views import second

urlpatterns = [
    path('uno/', first),
    path('dos/', second)
]