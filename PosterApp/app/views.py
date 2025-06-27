from rest_framework import viewsets
from .models import Poster, PosterStatus, StorageLocation
from .serializers import PosterSerializer, PosterStatusSerializer, StorageLocationSerializer

# ViewSets for the Poster, PosterStatus, and StorageLocation models
class PosterViewSet(viewsets.ModelViewSet):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterStatusViewSet(viewsets.ModelViewSet):
    queryset = PosterStatus.objects.all()
    serializer_class = PosterStatusSerializer

class StorageLocationViewSet(viewsets.ModelViewSet):
    queryset = StorageLocation.objects.all()
    serializer_class = StorageLocationSerializer