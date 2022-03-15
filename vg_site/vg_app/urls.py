from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pictures', views.PictureView)

urlpatterns = [
    path('picture/', views.picture_list),
    path('picture/<int:pk>/', views.picture_detail),
    path('', include(router.urls))
]