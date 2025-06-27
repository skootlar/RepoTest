from rest_framework import serializers
from .models import Poster, PosterStatus, StorageLocation

# Serializers for the Poster, PosterStatus, and StorageLocation models
class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'

class PosterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosterStatus
        fields = '__all__'

class StorageLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageLocation
        fields = '__all__'