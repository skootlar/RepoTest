from django.db import models

class Poster(models.Model):     # Represents a single movie poster
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    poster_design = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)

class PosterStatus(models.Model):       # Represents the status of a single poster
    STATUS_CHOICES = [
        ('RECEIVED', 'Received'),
        ('DISPLAYED', 'Displayed'),
        ('STORED', 'Stored'),
        ('DISCARDED', 'Discarded')
    ]
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateField(auto_now_add=True)

class StorageLocation(models.Model):    # Represents the storage location of a poster
    ZONE_CHOICES = [
        ('PRE-RELEASE', 'Pre-Release'),
        ('POSTER CASES', 'Poster Cases'),
        ('POST-RELEASE', 'Post-Release'),
        ('LONG-TERM', 'Long-Term')
    ]
    tube_number = models.CharField(max_length=50)
    zone = models.CharField(max_length=30, choices=ZONE_CHOICES)
