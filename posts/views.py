from django.shortcuts import render
from .models import Post, Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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
            comment.save()
            postURL = reverse("post", args=[id])
            return HttpResponseRedirect(postURL)

    form = CommentForm()
    return render(request, "posts/post.html", {"post": post, "form": form})


def tags(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, "posts/tags.html", {"tags": tag.post_set.all()})
