from django.views import generic
from vg_app.models import Picture, Artist
from random import randint
from django.db.models import Max, Q
from django.shortcuts import render, redirect
from .color_filter import color_is_near

def index(request):
    return render(request, 'index.html')

def random_picture_detail(request):
    picture = Picture.objects.all()
    max = picture.aggregate(Max('id'))
    pk = randint(1, max['id__max'])
    return redirect('vg_app:picture-detail', pk=pk)

class PictureListView(generic.ListView):
    model = Picture
    paginate_by = 10
    def get_queryset(self):
        title = self.request.GET.get('title')
        year = self.request.GET.get('year')
        artist = self.request.GET.get('artist')
        gallery = self.request.GET.get('gallery')
        color = self.request.GET.get('color')
        q = Q()
        if title:
            q &= Q(Title__icontains=title)
        if year:
            q &= Q(Year__icontains=year)
        if artist:
            q &= Q(Artist__Name__icontains=artist)
        if gallery:
            q &= Q(Gallery_name__icontains=gallery)
        object_list = Picture.objects.filter(q)
        if color:
            ids = [picture.id for picture in object_list if color_is_near(picture, color)]
            object_list = object_list.filter(id__in=ids)
        return object_list

class PictureDetailView(generic.DetailView):
    model = Picture

class ArtistListView(generic.ListView):
    model = Artist

class ArtistDetailView(generic.DetailView):
    model = Artist
