from django import template
register = template.Library()

@register.filter
def get_adjacent_pages(page_num, max_page_num):
    pages = [page for page in range(page_num-2, page_num+3) if page>0 and page<=max_page_num]
    return pages