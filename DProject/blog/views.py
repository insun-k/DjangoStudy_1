from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )


def singlePost_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/singlePost_page.html',
        {
            'post':post,
        }
    )