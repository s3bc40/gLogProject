from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from .forms import TextForm, FileForm
from .scripts import Process 

# Create your views here.
def home(request):
    return render(request,'annotation/home.html')

def process(request):
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        text_form = TextForm(request.POST)

        ## Check validity of forms
        if (text_form.is_valid()):
            return HttpResponse('<h1>Success text</h1>')
        if (file_form.is_valid()):
            uploaded_file = request.FILES['fasta_file']
            
            ## Save file in media root of server
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)

            ## Annotation process
            Process.processBlastx(fs.path(uploaded_file.name),uploaded_file.name)
            Process.parseBlast_XML(uploaded_file.name)

            ## WIP : delete files unused after process
            fs.delete(uploaded_file.name)
            return HttpResponse('<h1>Success file</h1><h2> Deleted : {}'.format(uploaded_file.name))

    # if a GET (or any other method) we'll create a blank form
    else:
        text_form = TextForm()
        file_form = FileForm()
    return render(request,'annotation/process.html',{'file_form':file_form,"text_form":text_form})
