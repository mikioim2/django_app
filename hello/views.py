from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params ={
        'title':'Hi You',
        'msg':'みたな',
        'goto':'next'
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title':'YoYo',
        'msg':'いもだよ',
        'goto':'index',
    }
    return render(request, 'hello/index.html', params)
# Create your views here.