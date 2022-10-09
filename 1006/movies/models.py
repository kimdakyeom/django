from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    running_time = models.IntegerField()
    RATE_CHOICES = (
        (1, '★'),         
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    )
    rate = models.IntegerField(max_length=10, choices=RATE_CHOICES)