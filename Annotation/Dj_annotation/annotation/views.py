from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import TextForm, FileForm
from .scripts import main,Fasta #add write quand y'aura le fichier dans les scripts

# Create your views here.
def home(request):
    return render(request,'annotation/home.html')

def process(request):
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        text_form = TextForm(request.POST)
        if (text_form.is_valid()):
            return HttpResponse('<h1>Success text</h1>')
        if (file_form.is_valid()):
            return HttpResponse('<h1>Success file</h1>')

    # if a GET (or any other method) we'll create a blank form
    else:
        text_form = TextForm()
        file_form = FileForm()
    return render(request,'annotation/process.html',{'file_form':file_form,"text_form":text_form})