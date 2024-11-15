from django.db import models
# event name, Duration, Genre, host name, Language, venue
# Create your models here.
class EventItem(models.Model):
    Name = models.CharField(max_length=50)
    Duration = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    hostName = models.CharField(max_length=50)
    Language = models.CharField(max_length=50)
    imageURL = models.URLField(max_length=300, default='https://example.com/default-image.jpg')
    Venue = models.CharField(max_length=50)