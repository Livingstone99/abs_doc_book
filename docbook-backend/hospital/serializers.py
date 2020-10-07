from rest_framework import serializers
from .models import Hospital, User, Specialist, Doctor, Appointment, Payment, Company, SpecialistType

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

# from .models import BaseUser
from .models import User
# from rest_framework.authtoken.models import Token

# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#
#         model = User
#         fields = ('id', 'username', 'email', 'password')
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    # first_name = serializers.CharField(max_length=255, min_length=2)
    # last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username',  'email', 'password', 'phone_number', 'user_type',
                  ]
# fields = ['username', 'first_name', 'last_name', 'email', 'password'
#                   ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ("Email is already in use, don't leave field empty")})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']
class AppointmentSerializer(serializers.ModelSerializer):
    reschedule_startime = serializers.DateTimeField(read_only=True)
    reschedule_endtime = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Appointment
        fields = ['user_name', 'venue', 'start_time', 'end_time',
                  'Aim', 'alert', 'user_doctor',
                  'user_specialist','reschedule_startime','reschedule_endtime']




