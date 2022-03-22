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
    paginate_by = 50

class PictureDetailView(generic.DetailView):
    model = Picture

class ArtistListView(generic.ListView):
    model = Artist
    paginate_by = 50

class ArtistDetailView(generic.DetailView):
    model = Artist

class PictureSearchView(generic.ListView):
    model = Picture
    def get_queryset(self):
        title = self.request.GET.get('title')
        year = self.request.GET.get('year')
        #artist = self.request.GET.get('artist')
        object_list = Picture.objects.filter(
        Q(Title__icontains=title) or Q(Year__icontains=year)
        )
        return object_list
