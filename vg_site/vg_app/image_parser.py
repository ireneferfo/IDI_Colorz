from .models import Picture, Artist
from .serializers import ArtistSerializer
from PIL import Image

def parse(picture):
    artist_pk = picture.data.get('Artist')
    artist = Artist.objects.get(pk=artist_pk)
    serializer = ArtistSerializer(artist)
    artist_url = serializer.data.get('Artist_url')
    year = picture.data.get('Year')
    picture_id = picture.data.get('Picture_ID')
    if year is not None:
        return f'resources/images/{artist_url}/{year}/{picture_id}.jpg'
    else:
        return f'resources/images/{artist_url}/unknown-year/{picture_id}.jpg'