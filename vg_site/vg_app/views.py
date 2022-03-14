from django.shortcuts import HttpResponse
from django.views import generic
from rest_framework import viewsets
from vg_app.serializers import PictureSerializer
from vg_app.models import Picture
from url_filter.filtersets import ModelFilterSet

# Create your views here.
class PictureView(viewsets.ReadOnlyModelViewSet):
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer

def index(request):
    return HttpResponse("Index")

def paintings(request):
    return HttpResponse("Paintings")