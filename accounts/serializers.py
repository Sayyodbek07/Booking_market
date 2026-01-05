from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ("username", "email", "password")

    def create(self, validated_data):
        account = Account(
            username=validated_data["username"],
            email=validated_data.get("email")
        )
        account.set_password(validated_data["password"])
        account.save()
        return account

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            account = Account.objects.get(username=data["username"])
        except Account.DoesNotExist:
            raise serializers.ValidationError("Username yoki parol noto‘g‘ri")

        if not account.check_password(data["password"]):
            raise serializers.ValidationError("Username yoki parol noto‘g‘ri")

        # JSON serializable formatga o‘tkazamiz
        refresh = RefreshToken.for_user(account)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": account.username,
            "email": account.email
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        try:
            token = RefreshToken(self.validated_data["refresh"])
            token.blacklist()
        except Exception:
            raise serializers.ValidationError("Token noto‘g‘ri yoki eskirgan")
