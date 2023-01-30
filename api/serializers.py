from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import AssetsModel, CheckIn, CheckOut, CheckOutAndReturn, DeviceLog, Company


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
#Assets Model Serializer
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsModel
        fields = '__all__'

#CheckIn Model Serializer
class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'

#CheckOut Model Serializer       
class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = '__all__'

#CheckOut And Return Model Serializer        
class CheckOutAndReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOutAndReturn
        fields = '__all__'

#Device Log Model Serializer
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'

#Company Model Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'    
