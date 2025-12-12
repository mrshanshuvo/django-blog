from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

posts = [
    {
        'id': 1,
        'title': 'How to Learn Python Fast',
        'content': 'Start with the basics, practice regularly, and build small projects. Consistency is more important than speed.'
    },
    {
        'id': 2,
        'title': 'React vs Vue: Which One to Choose?',
        'content': 'React is backed by Facebook and has a huge ecosystem. Vue is simpler to learn and offers great developer experience. Both are excellent choices depending on the project.'
    },
    {
        'id': 3,
        'title': 'Why Sleep Matters for Productivity',
        'content': 'Lack of sleep reduces focus, creativity, and decision making. Sleeping 7-8 hours boosts mental performance and memory.'
    },
    {
        'id': 4,
        'title': 'Top 5 Tips for Job Interviews',
        'content': 'Research the company, practice common questions, be confident, show your skills through examples, and follow up with a thank-you email.'
    }
]

categories = [
  "Programming",
  "Food",
  "Travel"
]
# Create your views here.
def home(request):
  return render(request, 'posts/index.html', {'posts' : posts, "categories": categories})

def post(request, id):
  valid_id = False
  for post in posts:
    if post['id'] == id:
      post_dict = post
      valid_id = True
      break
  if valid_id:
    return render(request, 'posts/post.html', {'post': post_dict, "categories": categories})
  else:
    raise Http404()
  
  
