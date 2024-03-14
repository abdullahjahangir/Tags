from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class SignUpSerializers(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    password_again = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ["email", "username", "password", "password_again"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_again"]:
            raise ValidationError("Passwords Does Not Match")
        return super().validate(attrs)

    def create(self, validate_data):
        password = validate_data.pop("password")
        password_again = validate_data.pop("password_again")
        user = super().create(validate_data)
        user.set_password(password)
        user.save()
        return user
