from django.shortcuts import render, redirect


def find(request):
    return render(request, 'find.html')
