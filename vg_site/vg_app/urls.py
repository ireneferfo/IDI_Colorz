from django.urls import path
from . import views

app_name = 'vg_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('picture/', views.PictureListView.as_view(), name='picture'),
    path('picture/<int:pk>', views.PictureDetailView.as_view(), name='picture-detail'),
    path('picture/random/', views.random_picture_detail, name='random'),
    path('artist/', views.ArtistListView.as_view(), name='artist'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('picture/export-csv/', views.download_picture_csv, name='picture-export-csv'),
    path('picture/export-json/', views.download_picture_json, name='picture-export-json'),
    path('arist/export-csv/', views.download_artist_csv, name='artist-export-csv'),
    path('artist/export-json/', views.download_artist_json, name='artist-export-json')
]
