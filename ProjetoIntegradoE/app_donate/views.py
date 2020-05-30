from django.shortcuts import render, redirect


def donate(request):
    return render(request, 'donate.html')


def donateType(request):
    return render(request, 'donate_type.html')
