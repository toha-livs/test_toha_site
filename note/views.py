from django.shortcuts import render, redirect
from .models import Posts
from . import xviews


def home(request):
    if request.method == "GET":
        posts = Posts.objects.values()
        context = {'posts': xviews.get_list_posts(posts)}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        texts = request.POST.get('text')
        confirm_text = Posts(body=texts)
        confirm_text.save()
        return redirect('home')


