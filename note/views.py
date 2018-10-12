from django.shortcuts import render, redirect
from .models import Posts
from . import xviews


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.renderers import JSONRenderer


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


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        posts = Posts.objects.values()
        context = xviews.get_list_posts(posts)
        context = xviews.get_for_api(context)
        return Response(context)

    elif request.method == 'POST':
        text = request.POST.get('body')
        print(text)
        confirm_text = Posts(body=text)
        confirm_text.save()
        context = {'status': 'success', 'text': 'Your message is confirm!'}
        return Response(context)
