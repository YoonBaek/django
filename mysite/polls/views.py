from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("안녕하세요. 이 곳은 polls index 입니다.")