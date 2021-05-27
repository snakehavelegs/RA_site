from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *



router = routers.DefaultRouter()
router.register(r'offers', views.OfferViewSet)
router.register(r'types', views.TypeViewSet)

urlpatterns = [
	path('home/', home_view),
	path('offers/', offers_view),
	path('reservation/', reservation_view),
	path('aboutme/', aboutme_view),
	path('gallery/', gallery_view),
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls',
		namespace='rest_framework'))
	]
