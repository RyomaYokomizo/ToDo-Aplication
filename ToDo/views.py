from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def index(request):
    data = ToDo.objects.all
    return render(request, 'ToDo/index.html',{'data': data})
