from rest_framework import serializers
from binpaste.models import Bin

class BinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bin
        fields = ['title', 'text',  'pub_date', 'language']
