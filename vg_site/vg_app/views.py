from django.shortcuts import HttpResponse
from django.views import generic
from rest_framework import viewsets
from vg_app.serializers import PictureSerializer
from vg_app.models import Picture, Artist
from url_filter.filtersets import ModelFilterSet
from django.http import JsonResponse
from .image_parser import parse
from random import randint
from django.db.models import Max, Q
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def random_picture_detail(request):
    picture = Picture.objects.all()
    max = picture.aggregate(Max('id'))
    pk = randint(1, max['id__max'])
    return redirect('vg_app:picture-detail', pk=pk)

class PictureListView(generic.ListView):
    model = Picture
    def get_queryset(self):
        title = self.request.GET.get('title')
        year = self.request.GET.get('year')
        artist = self.request.GET.get('artist')
        q = Q()
        if title:
            q &= Q(Title__icontains=title)
        if year:
            q &= Q(Year__icontains=year)
        if artist:
            q &= Q(Artist__Name__icontains=artist)
        object_list = Picture.objects.filter(q)
        return object_list

class PictureDetailView(generic.DetailView):
    model = Picture

class ArtistListView(generic.ListView):
    model = Artist

class ArtistDetailView(generic.DetailView):
    model = Artist
