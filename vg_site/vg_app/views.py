from django.shortcuts import HttpResponse
from django.views import generic
from rest_framework import viewsets
from vg_app.serializers import PictureSerializer
from vg_app.models import Picture, Artist
from url_filter.filtersets import ModelFilterSet
from django.http import JsonResponse
from .image_parser import parse
from random import randint
from django.db.models import Max
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')


class PictureListView(generic.ListView):
    model = Picture
    paginate_by = 50


class PictureDetailView(generic.DetailView):
    model = Picture

class ArtistListView(generic.ListView):
    model = Artist

    paginate_by = 50


class ArtistDetailView(generic.DetailView):
    model = Artist

def random_picture_detail(request):
    picture = Picture.objects.all()
    max = picture.aggregate(Max('id'))
    pk = randint(1, max['id__max'])
    return redirect('vg_app:picture-detail', pk=pk)
