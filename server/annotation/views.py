from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from django import forms
from .forms import TextForm, FileForm, RadioSelect
from .scripts import Process 
import os

# Create your views here.
def home(request):
    return render(request,'annotation/home.html')

def process(request):
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        text_form = TextForm(request.POST)
        radio_form = RadioSelect(request.POST)
        blast_results = None

        ## Check validity of forms
        if (text_form.is_valid()):
            text = text_form.cleaned_data["fasta_text"]
            filePath = Process.writeFasta(text)
            ## Annotation process
            Process.processBlastx(filePath)
            blast_results = Process.parseBlast_XML()
            os.remove(filePath)

        elif (file_form.is_valid()):
            uploaded_file = request.FILES['fasta_file']
            
            ## Save file in media root of server
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)

            ## Annotation process
            Process.processBlastx(fs.path(uploaded_file.name))
            blast_results = Process.parseBlast_XML()

            ## WIP : delete files unused after process
            fs.delete(uploaded_file.name)
        return render(request,'annotation/result.html',{"blast_results" : blast_results})
    # if a GET (or any other method) we'll create a blank form
    else:
        text_form = TextForm()
        file_form = FileForm()
        radio_form = RadioSelect()
    return render(request,'annotation/process.html',{'file_form':file_form,"text_form":text_form,"radio_form":radio_form})

def masonVisu(request):
    return render(request,'annotation/visuAnnot.html')
