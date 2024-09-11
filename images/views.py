from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.contrib import messages


def upload_image(request):

    form = ImageForm()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.is_approved = True
            image.save()
            messages.success(request, "L'image a été publier avec succès.")
            return redirect("home")
        else:
            if not messages.get_messages(request):
                messages.error(request, "❌ Ce genre d'images est interdit sur cette plateforme !!!")
    return render(request, "upload_image.html", {"form": form})


def home(request):
    images = Image.objects.filter(is_approved=True)
    return render(request, "image_list.html", {"images": images})
