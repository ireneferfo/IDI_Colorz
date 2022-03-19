from django.shortcuts import HttpResponse
from django.views import generic
from rest_framework import viewsets
from vg_app.serializers import PictureSerializer
from vg_app.models import Picture
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


class PictureView(viewsets.ReadOnlyModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


def picture_list(request):
    picture = Picture.objects.all()
    serializer = PictureSerializer(picture, many=True)
    return JsonResponse(serializer.data, safe=False)


def picture_detail(request, pk):
    try:
        picture = Picture.objects.get(pk=pk)
    except Picture.DoesNotExist:
        return HttpResponse(status=404)
    serializer = PictureSerializer(picture)
    image = parse(serializer)
    with open(image, 'rb') as i:
        return HttpResponse(i.read(), content_type='image/jpeg')


def random_picture_detail(request):
    picture = Picture.objects.all()
    max = picture.aggregate(Max('id'))
    pk = randint(1, max['id__max'])
    return redirect('vg_app:picture-detail', pk=pk)
