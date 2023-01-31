from django.urls import path, include
from .views import RegisterAPI
from api import views
from rest_framework.routers import DefaultRouter


#Register Routers
router = DefaultRouter()

router.register('api', views.AssetViewSet, basename='assetapi')

router.register('checkin', views.CheckInViewSet, basename='checkinaip')

router.register('checkout', views.CheckOutViewSet, basename='checkoutapi')

router.register('checkoutandreturn', views.CheckOutAndReturnSerializerViewSet, basename='checkocutandreturn')

router.register('devicelog', views.DeviceLogViewSet, basename='devicelog')

router.register('company', views.CompanyCViewSet, basename='company')


urlpatterns = [

    path('', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]