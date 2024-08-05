from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')
def  dash(request):
    return render(request,'dash.html')