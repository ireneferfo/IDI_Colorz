from rest_framework import serializers
from composite_field.rest_framework_support import CompositeFieldSerializer


from vg_app.models import Picture, Artist, Gallery, Color

class PictureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Picture
    fields = '__all__'
    
    
# class AstrometrySerializer(serializers.ModelSerializer):
#   ctype1 = CompositeFieldSerializer()
#   ctype2 = CompositeFieldSerializer()
  
#   class Meta:
#     model = Astrometry
#     exclude = [f.name for g in Astrometry._meta.get_fields() 
#                if hasattr(g, 'subfields') 
#                for f in g.subfields.values()] 
    
