from django.shortcuts import render

from new_app.forms import FurnitureForms
from new_app.models import furniture


# Create your views here.
def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')
def  dash(request):

    return render(request,'dash.html')

def submit(request):
    form = FurnitureForms()
    return render(request, 'submit.html', {'form': form})

