import datetime

from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'last_login')


class CustomRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password', 'password2')
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        if CustomUser.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError(
                {"username": "User with this username already exists."})
        if CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {"email": "User with this email already exists."})
        return attrs
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop("password2", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.last_login = datetime.datetime.now()
        instance.save()
        return instance

