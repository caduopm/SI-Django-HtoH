from django.shortcuts import render, redirect


def adopt(request):
    return render(request, 'adopt.html')
