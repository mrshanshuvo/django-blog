from django.shortcuts import render
from .forms import AuthorsForm

# Create your views here.
def home(request):
  form = AuthorsForm()
  return render(request, 'authors/home.html', {'form': form})