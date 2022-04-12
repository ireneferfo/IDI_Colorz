from django import template
from ..models import Artist
register = template.Library()

@register.filter
def get_adjacent_pages(page_num, max_page_num):
    pages = [page for page in range(page_num-2, page_num+3) if page>0 and page<=max_page_num]
    return pages

@register.simple_tag
def get_artist_list():
    artists = Artist.objects.all()
    l = []
    for artist in artists:
        l.append(artist.Name)
    print(l)
    return l