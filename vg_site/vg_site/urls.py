from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('vg_app.urls', namespace='vg_app')),
    path('admin/', admin.site.urls)
]
