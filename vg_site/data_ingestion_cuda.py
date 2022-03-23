import json
import os
import django
from get_colors_cuda import extract_colors
from tqdm import tqdm
from sklearnex import patch_sklearn
patch_sklearn()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vg_site.settings')
django.setup()

from vg_app.models import *
from datetime import datetime, timedelta


with open('resources/artists.json', 'r') as a:
  ARTISTS = json.load(a)

for artist in ARTISTS:
    artist_object = Artist.objects.create(
        Artist_ID = artist['contentId'],
        Name = artist['artistName'],
        Artist_url = artist['url'],
        Birth_date = (datetime.fromtimestamp(0) + timedelta(seconds=int(artist['birthDay'][6:-5]))).date(),
        Death_date = (datetime.fromtimestamp(0) + timedelta(seconds=int(artist['deathDay'][6:-5]))).date()
    )

    with open(f"resources/{artist['url']}.json", 'r', encoding="utf8") as p:
        PICTURES = json.load(p)

    for picture in tqdm(PICTURES):
    
        picture_object = Picture.objects.create(
            Picture_ID = picture['contentId'],
            Title = picture['title'],
            Year = picture['completitionYear'],
            Artist = artist_object,
            Width = picture['width'],
            Height = picture['height'],
            Location = picture['location'],
            Genre = picture['genre'],
            Style = picture['style'],
            Size_x = picture['sizeX'],
            Size_y = picture['sizeY'],
            Tags = picture['tags']
        )

        if picture_object.Year is not None:
            d = extract_colors(f'vg_app/static/images/{artist_object.Artist_url}/{picture_object.Year}/{picture_object.Picture_ID}.jpg')
        else:
            d = extract_colors(f'vg_app/static/images/{artist_object.Artist_url}/unknown-year/{picture_object.Picture_ID}.jpg')

        for k, v in d.items():
            color_object = Color.objects.create(
                Color = k,
                Quantity = v
            )
            picture_object.Color.add(color_object)

        