from django.shortcuts import render
from django.http import JsonResponse
from .translator import translator
def getdata(request,input):
    result=translator(input)
    print(result)
    return JsonResponse({'data':result})
def home(request):
    return render(request,'mainapp/home.html')

def about(request):
    return render(request,'mainapp/about.html')

def docs(request):
    return render(request,'mainapp/docs.html')
