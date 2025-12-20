from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    all_posts = Post.objects.all().order_by("-id")
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get("p", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "posts/index.html", {"posts": page_obj})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post.html", {"post": post})
