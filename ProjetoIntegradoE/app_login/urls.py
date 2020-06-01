from django.urls import path

from .views import login, register, registerOng1, registerOng2, registerUser1, registerUser2, resetPassword

urlpatterns = [
    path('', login, name='login'),
    path('register', register, name='register'),
    path('registerOng1', registerOng1, name='registerOng1'),
    path('registerOng2', registerOng2, name='registerOng2'),
    path('registerUser1', registerUser1, name='registerUser1'),
    path('registerUser2', registerUser2, name='registerUser2'),
    path('resetPassword', resetPassword, name='resetPassword'),
]
