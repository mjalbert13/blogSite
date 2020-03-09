from django.shortcuts import render
import datetime
# Create your views here.

posts = [
    {
        'author': 'Matt',
        'title': 'Post 1',
        'content': "First post",
        'date': "3/4/17"
    },
    {
        'author': 'Joe',
        'title': 'Post 2',
        'content': "hello Worlds",
        'date': "3/14/19"
    },
    {
        'author': 'Bill',
        'title': 'Post 3',
        'content': "Post Up",
        'date': "3/12/20"
    },

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})