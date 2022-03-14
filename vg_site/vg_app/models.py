from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Artist(models.Model):
    Artist_ID = models.IntegerField(default=0, unique=True)
    Name = models.CharField(max_length=50)
    Birth_date = models.DateField()
    Death_date = models.DateField()

class Gallery(models.Model):
    Name = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Coordinates_x = models.FloatField(blank=True, null=True)
    Coordinates_y = models.FloatField(blank=True, null=True)

class Picture(models.Model):
    Picture_ID = models.IntegerField(default=0, unique=True)
    Title = models.CharField(max_length=50)
    Year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1000),
    MaxValueValidator(timezone.now().year)])
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Width = models.PositiveSmallIntegerField()
    Height = models.PositiveSmallIntegerField()
    Location = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50, blank=True, null=True)
    Style = models.CharField(max_length=50, blank=True, null=True)
    Size_x = models.FloatField(blank=True, null=True)
    Size_y = models.FloatField(blank=True, null=True)    
    Gallery_name = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=200)

class Color(models.Model):
    Picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    Color = models.CharField(max_length=6)
    Quantity = models.PositiveIntegerField(default=0)