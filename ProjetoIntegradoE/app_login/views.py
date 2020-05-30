from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def registerOng1(request):
    return render(request, 'register_ong_1.html')


def registerOng2(request):
    return render(request, 'register_ong_2.html')


def registerUser1(request):
    return render(request, 'register_user_1.html')


def registerUser2(request):
    return render(request, 'register_user_2.html')


def resetPassword(request):
    return render(request, 'reset_password.html')
