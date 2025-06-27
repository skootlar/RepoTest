from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PosterViewSet, PosterStatusViewSet, StorageLocationViewSet

router = DefaultRouter()
router.register(r'posters', PosterViewSet)
router.register(r'statuses', PosterStatusViewSet)
router.register(r'storage', StorageLocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]