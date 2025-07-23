from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import UploadImageForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('images'):
                GalleryImage.objects.create(image=image)
    else:
        form = UploadImageForm()

    gallery = GalleryImage.objects.all()
    return render(request, 'gallery_with_upload.html', {'form': form, 'gallery': gallery})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
