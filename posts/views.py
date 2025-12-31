from django.shortcuts import render
from .models import Post, Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


# Create your views here.
def home(request):
    all_posts = Post.objects.all().order_by("-id")
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get("p", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "posts/index.html", {"posts": page_obj})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            postURL = reverse("post", args=[id])
            return HttpResponseRedirect(postURL)

    form = CommentForm()
    return render(
        request,
        "posts/post.html",
        {"post": post, "form": form, "comments": post.comment_set.all()},
    )


def tags(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, "posts/tags.html", {"tags": tag.post_set.all()})


def search(request):
    q = request.GET.get("q", None)
    page_number = request.GET.get("p", 1)
    posts = Post.objects.filter(
        Q(post_title__icontains=q) | Q(post_content__icontains=q)
    ).order_by("-id")
    paginator = Paginator(posts, 4)
    page_obj = paginator.get_page(page_number)
    return render(request, "posts/search.html", {"posts": page_obj, "q": q})
