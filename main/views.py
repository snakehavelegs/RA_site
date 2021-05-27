from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import OfferSerializer,TypeSerializer
from .models import Offer, Type

class OfferViewSet(viewsets.ModelViewSet):
	queryset = Offer.objects.all().order_by('name')
	serializer_class = OfferSerializer

class TypeViewSet(viewsets.ModelViewSet):
	queryset = Type.objects.all().order_by('kindof')
	serializer_class = TypeSerializer

def home_view(request):
	return render(request, 'home/index.html')

def offers_view(request):
	return render(request, 'offers/offers.html')

def reservation_view(request):
	return render(request, 'reservation/reservation.html')

def aboutme_view(request):
	return render(request, 'aboutme/aboutme.html')

def gallery_view(request):
	return render(request, 'gallery/gallery.html')