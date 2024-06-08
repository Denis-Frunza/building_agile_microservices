from rest_framework import serializers
from user_auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

from user_auth.enums import StatusChoices, GenderChoices

class CustomRegisterSerializer(RegisterSerializer):
    status = serializers.ChoiceField(
        choices=StatusChoices.choices()
    )
    status_description = serializers.CharField(
        source='get_status_display',
        read_only=True
    )
    gender = serializers.ChoiceField(
        choices=GenderChoices.choices()
    )
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()

    class Meta:
        model = User
        fields = ['password', 'username', 'first_name', 'last_name',
                'email', 'phone_number', 'gender', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'gender': self.validated_data.get('gender', ''),
            'status': self.validated_data.get('status', ''),
        
        }
    def validate(self, data):
        email = data.get('email')
        phone_number = data.get('phone_number')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email address is already in use.")

        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("Phone number is already in use.")

        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}, 
            'is_superuser': {'read_only': True},
            'is_staff': {'read_only': True},
            'groups': {'read_only': True},
            'user_permissions': {'read_only': True},
            'last_login': {'read_only': True},
        }
