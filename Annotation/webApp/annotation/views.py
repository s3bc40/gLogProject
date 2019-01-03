from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author' : 'SGC',
        'title' : 'First Post 1',
        'content' : 'First post content',
        'date_posted': '01/03/2019'
    },
    {
        'author' : 'BZH',
        'title' : 'First Post 2',
        'content' : 'Second post content',
        'date_posted': '01/02/2019'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'annotation/home.htm', context)

def about(request):
    return render(request, 'annotation/about.htm', {'title' : 'About'})