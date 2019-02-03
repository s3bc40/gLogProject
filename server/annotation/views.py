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

        ## Check validity of forms
        if (text_form.is_valid()):
            text = text_form.cleaned_data["fasta_text"]
            filePath = Process.writeFasta(text)
            ## Annotation process
            Process.processBlastx(filePath)
            Process.parseBlast_XML()
            blast_results=Process.getResults()
            os.remove(filePath)
            return HttpResponse('<h1>Success text</h1><h2> Deleted : {}</h2><h3>Blast results :</h3><h4> {}</h4>'.format(filePath,blast_results))

        elif (file_form.is_valid()):
            uploaded_file = request.FILES['fasta_file']
            
            ## Save file in media root of server
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)

            ## Annotation process
            Process.processBlastx(fs.path(uploaded_file.name))
            Process.parseBlast_XML()

            ## WIP : delete files unused after process
            fs.delete(uploaded_file.name)
            blast_results=Process.getResults()
            return HttpResponse('<h1>Success file</h1><h2> Deleted : {}</h2><h3>Blast results :</h3><h4> {}</h4>'.format(uploaded_file.name,blast_results))

    # if a GET (or any other method) we'll create a blank form
    else:
        text_form = TextForm()
        file_form = FileForm()
        radio_form = RadioSelect()
    return render(request,'annotation/process.html',{'file_form':file_form,"text_form":text_form,"radio_form":radio_form})
