from django.shortcuts import render, redirect


def chart(request):
    return render(request, 'charts.html')
