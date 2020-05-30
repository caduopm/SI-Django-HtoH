from django.urls import path

from .views import adopt

urlpatterns = [
    path('', adopt, name='adopt'),
]
