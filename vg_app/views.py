from django.views import generic
from vg_app.models import Picture, Artist, Color
from random import randint
from django.db.models import Max, Q
from django.shortcuts import render, redirect
from .color_filter import color_is_near
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from django.conf import settings
import csv


def index(request):
    return render(request, 'index.html')


def random_picture_detail(request):
    picture = Picture.objects.all()
    max = picture.aggregate(Max('id'))
    pk = randint(1, max['id__max'])
    return redirect('vg_app:picture-detail', pk=pk)


def download_picture_csv(request):
    response = HttpResponse(content_type='text/csv',
                            headers={'Content-Disposition': 'attachment; filename="pictures.csv"'})
    model = Picture
    model_fields = model._meta.fields + model._meta.many_to_many
    field_names = [field.name for field in model_fields if field.name != 'id']

    writer = csv.writer(response)
    writer.writerow(field_names)
    title = request.GET.get('title')
    year = request.GET.get('year')
    artist = request.GET.get('artist')
    gallery = request.GET.get('gallery')
    tags = request.GET.get('tags')
    color = request.GET.get('color')
    q = Q()
    if title:
        q &= Q(Title__icontains=title)
    if year:
        q &= Q(Year__icontains=year)
    if artist:
        q &= Q(Artist__Name__icontains=artist)
    if gallery:
        q &= Q(Gallery_name__icontains=gallery)
    if tags:
        q &= Q(Tags__icontains=tags)
    object_list = Picture.objects.filter(q)
    if color:
        ids = [picture.id for picture in object_list if color_is_near(picture, color)]
        object_list = object_list.filter(id__in=ids)

    for row in object_list:
        values = []
        for field in field_names:
            if field == "Artist":
                value = row.Artist.Name
            elif field == "Color":
                value = '{'
                for color in row.Color.all():
                    value += color.Color + ': ' + str(color.Quantity) + ', '
                value = value[:-2] + '}'
            else:
                value = getattr(row, field)
            if value is None:
                value = ''
            values.append(value)
        writer.writerow(values)

    return response


def download_picture_json(request):
    title = request.GET.get('title')
    year = request.GET.get('year')
    artist = request.GET.get('artist')
    gallery = request.GET.get('gallery')
    tags = request.GET.get('tags')
    color = request.GET.get('color')
    q = Q()
    if title:
        q &= Q(Title__icontains=title)
    if year:
        q &= Q(Year__icontains=year)
    if artist:
        q &= Q(Artist__Name__icontains=artist)
    if gallery:
        q &= Q(Gallery_name__icontains=gallery)
    if tags:
        q &= Q(Tags__icontains=tags)
    object_list = Picture.objects.filter(q)
    if color:
        ids = [picture.id for picture in object_list if color_is_near(picture, color)]
        object_list = object_list.filter(id__in=ids)

    serializer = PictureSerializer(instance=object_list, many=True)
    picture_json = JSONRenderer().render(serializer.data)
    return HttpResponse(picture_json, content_type='application/json',
                        headers={'Content-Disposition': 'attachment; filename="picture.json"'})


def download_picture_xml(request):
    title = request.GET.get('title')
    year = request.GET.get('year')
    artist = request.GET.get('artist')
    gallery = request.GET.get('gallery')
    tags = request.GET.get('tags')
    color = request.GET.get('color')
    q = Q()
    if title:
        q &= Q(Title__icontains=title)
    if year:
        q &= Q(Year__icontains=year)
    if artist:
        q &= Q(Artist__Name__icontains=artist)
    if gallery:
        q &= Q(Gallery_name__icontains=gallery)
    if tags:
        q &= Q(Tags__icontains=tags)
    object_list = Picture.objects.filter(q)
    if color:
        ids = [picture.id for picture in object_list if color_is_near(picture, color)]
        object_list = object_list.filter(id__in=ids)

    serializer = PictureSerializer(instance=object_list, many=True)
    picture_xml = XMLRenderer().render(serializer.data)
    return HttpResponse(picture_xml, content_type='text/xml',
                            headers={'Content-Disposition': 'attachment; filename="picture.xml"'})


def download_artist_csv(request):
    response = HttpResponse(content_type='text/csv',
                            headers={'Content-Disposition': 'attachment; filename="artist.csv"'})
    model = Artist
    model_fields = model._meta.fields + model._meta.many_to_many
    field_names = [field.name for field in model_fields if field.name != 'id']

    writer = csv.writer(response)
    writer.writerow(field_names)
    object_list = Artist.objects.all()

    for row in object_list:
        values = []
        for field in field_names:
            value = getattr(row, field)
            if value is None:
                value = ''
            values.append(value)
        writer.writerow(values)

    return response


def download_artist_json(request):
    object_list = Artist.objects.all()
    serializer = ArtistSerializer(instance=object_list, many=True)
    artist_json = JSONRenderer().render(serializer.data)
    return HttpResponse(artist_json, content_type='application/json',
                        headers={'Content-Disposition': 'attachment; filename="artist.json"'})


def download_artist_xml(request):
    object_list = Artist.objects.all()
    serializer = ArtistSerializer(instance=object_list, many=True)
    artist_xml = XMLRenderer().render(serializer.data)
    return HttpResponse(artist_xml, content_type='text/xml',
                        headers={'Content-Disposition': 'attachment; filename="artist.xml"'})

def get_static(path):
    if settings.DEBUG:
        return 'static/' + path
    else:
        return 'staticfiles/' + path

def download_image(request):
    artist = request.GET.get('artist')
    year = request.GET.get('year')
    id = request.GET.get('id')
    fl_path = get_static('images/' + artist + '/' + year + '/' + id + '.jpg')
    q = Q(Picture_ID__icontains=id)
    object_list = Picture.objects.filter(q)
    filename = object_list[0].Title.replace(' ', '_')

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response


class PictureListView(generic.ListView):
    model = Picture
    paginate_by = 10

    def get_queryset(self):
        title = self.request.GET.get('title')
        year = self.request.GET.get('year')
        artist = self.request.GET.get('artist')
        gallery = self.request.GET.get('gallery')
        paintedin = self.request.GET.get('paintedin')
        tags = self.request.GET.get('tags')
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
        if paintedin:
            q &= Q(Location__icontains=paintedin)
        if tags:
            q &= Q(Tags__icontains=tags)
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


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("Artist_ID", "Name", "Artist_url", "Birth_date", "Death_date", "Image", "Wikipedia")


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("Color", "Quantity")


class PictureSerializer(serializers.ModelSerializer):
    Color = ColorSerializer(many=True, read_only=True)
    Artist = serializers.CharField(source='Artist.Name')
    class Meta:
        model = Picture
        fields = (
            "Picture_ID", "Title", "Year", "Artist", "Width", "Height", "Location", "Genre", "Style", "Size_x",
            "Size_y",
            "Gallery_name", "Tags", "Color")
        depth = 1
