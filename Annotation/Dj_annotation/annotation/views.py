from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'annotation/home.html')

def process(request):
    return render(request,'annotation/process.html')