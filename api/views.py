from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
#Import api Models
from api.models import AssetsModel, CheckIn, CheckOut, CheckOutAndReturn, DeviceLog, Company
#Impost api serializers
from api.serializers import  RegisterSerializer, UserSerializer, AssetSerializer, CheckInSerializer, CheckOutSerializer, CheckOutAndReturnSerializer, DeviceLogSerializer, CompanySerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#Company model viewset
class CompanyCViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

#Assets mosel viewset
class AssetViewSet(viewsets.ModelViewSet):
    queryset = AssetsModel.objects.all()
    serializer_class = AssetSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

#Checkin model viewset  
class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
#CheckOut model viewset   
class CheckOutViewSet(viewsets.ModelViewSet):
    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

#CheckIn and Return model viewset
class CheckOutAndReturnSerializerViewSet(viewsets.ModelViewSet):
    queryset = CheckOutAndReturn.objects.all()
    serializer_class = CheckOutAndReturnSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

#Device Log model viewset
class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

