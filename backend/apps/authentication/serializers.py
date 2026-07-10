from rest_framework import serializers
from .models import User
from rest_framework_simplejwt import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {
    "password": {
        "write_only": True
    }
}
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self,data):
        username = data['username']
        user = User.objects.filter(username=username).first()
        if not user:
            raise serializers.ValidationError(
                'invalid Username or password'
            )
        password = data['password']
        if not user.check_password(password):
            raise serializers.ValidationError(
                'invalid Username or password'
            )
        data['user'] = user
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        try:
            token = RefreshToken(data['refresh'])
            token.blacklist()
        except Exception:
            raise serializers.ValidationError(
                'invalid token'
            )
        return data