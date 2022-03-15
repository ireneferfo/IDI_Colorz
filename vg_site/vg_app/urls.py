from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'vg_app'

router = DefaultRouter()
router.register(r'pictures', views.PictureView)

urlpatterns = [
    path('picture/', views.picture_list, name='picture'),
    path('picture/<int:pk>/', views.picture_detail),
    path('picture/random/', views.random_picture_detail, name='random'),
    path('', include(router.urls))
]