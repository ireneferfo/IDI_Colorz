from django.shortcuts import HttpResponse
from django.views import generic
from rest_framework import viewsets
from vg_app.serializers import PictureSerializer
from vg_app.models import Picture
from url_filter.filtersets import ModelFilterSet
from django.http import JsonResponse
from .image_parser import parse

# Create your views here.
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
	# return JsonResponse(serializer.data.get('Title'), safe=False)

def index(request):
    return HttpResponse("Index")
