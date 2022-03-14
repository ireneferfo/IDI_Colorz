import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vg_site.settings')
django.setup()

from vg_app.models import *
from datetime import datetime


with open('resources/artists.json', 'r') as a:
  ARTISTS = json.load(a)

for artist in ARTISTS:
    Artist_ID = artist['contentId']
    Name = artist['artistName']
    Birth_date =  datetime.fromtimestamp(int(artist['birthDay'][6:-5])).date()  
    Death_date = datetime.fromtimestamp(int(artist['deathDay'][6:-5])).date()
    url = artist['url']

    artist_object = Artist.objects.create(
        Artist_ID = Artist_ID,
        Name = Name,
        Birth_date = Birth_date,
        Death_date = Death_date
    )

    with open(f'resources/{url}.json', 'r') as p:
        PICTURES = json.load(p)

    for picture in PICTURES:
    
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


