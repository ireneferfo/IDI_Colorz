from django import template
from ..models import Artist

register = template.Library()


@register.filter
def get_adjacent_pages(page_num, max_page_num):
    pages = [page for page in range(page_num - 2, page_num + 3) if page > 0 and page <= max_page_num]
    return pages


@register.inclusion_tag("picture_list.html")
def get_artist_list():
    artists = Artist.objects.all().values()
    art_list = []
    for artist in artists:
        art_list.append(artist['Name'])
    return art_list
