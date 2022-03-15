from rest_framework import serializers
from composite_field.rest_framework_support import CompositeFieldSerializer


from vg_app.models import Picture, Artist, Gallery, Color

class PictureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Picture
		fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = '__all__'