from hashlib import new
import re
from django.shortcuts import render, redirect
from .models import info, PostForm

# Create your views here.
def home(request):
  litinfo = info.objects.all()
  return render(request, 'home.html', {'litinfo': litinfo})

def uploadform(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    details = request.POST.get('details')
    littype = request.POST.get('littype')
    image = request.FILES.get('image')

    new_object = info.objects.create(name=name, details=details, littype=littype, image=image)
    new_object.save()

  return render(request, 'uploadform.html', {})