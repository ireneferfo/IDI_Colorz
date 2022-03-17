from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'vg_app'

router = DefaultRouter()
router.register(r'pictures', views.PictureView)

urlpatterns = [
    path('', views.index, name='index'),
    path('picture/', views.PictureListView
         .as_view(), name='picture'),
    path('picture/<int:pk>', views.PictureDetailView.as_view(), name='picture-detail'),
    path('picture/random/', views.random_picture_detail, name='random')
]