from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def submit(request):
    info=request.POST['info']
    import src.salary_equivilant
    return render(request, 'home.html')
