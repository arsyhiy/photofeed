from django.shortcuts import render
from . import models
from django.views import generic

def index(request):
  
  images = models.image.objects.all()
  user = models.forum_user.objects.all()
  return render(request,'index.html',{
    'images': images,
    'user': user},
  )

class imagelistView(generic.ListView):
    """"""
    model = models.image 
    paginate_by = 10