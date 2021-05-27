from rest_framework import serializers
from .models import Offer, Type

class OfferSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Offer
		fields = ['name']

class TypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Type
		fields = ('typeoffer', 'kindof', 'description', 'price')