from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Artist(models.Model):
    Artist_ID = models.IntegerField(default=0, unique=True)
    Name = models.CharField(max_length=50)
    Artist_url = models.CharField(max_length=100)
    Birth_date = models.DateField()
    Death_date = models.DateField()

class Gallery(models.Model): # togliere?
    Name = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Coordinates_x = models.FloatField(blank=True, null=True)
    Coordinates_y = models.FloatField(blank=True, null=True)

class Color(models.Model):
    Color = models.CharField(max_length=6)
    Quantity = models.FloatField(default=0)

class Picture(models.Model):
    Picture_ID = models.IntegerField(default=0, unique=True)
    Title = models.CharField(max_length=50)
    Year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1000),
    MaxValueValidator(timezone.now().year)], null=True)
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Width = models.PositiveSmallIntegerField()
    Height = models.PositiveSmallIntegerField()
    Location = models.CharField(max_length=50, null=True)
    Genre = models.CharField(max_length=50, blank=True, null=True)
    Style = models.CharField(max_length=50, blank=True, null=True)
    Size_x = models.FloatField(blank=True, null=True)
    Size_y = models.FloatField(blank=True, null=True)    
    Gallery_name = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=200, null=True)
    Color = models.ManyToManyField(Color)