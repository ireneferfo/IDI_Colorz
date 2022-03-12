from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index")

def page(request):
    return HttpResponse("Page")