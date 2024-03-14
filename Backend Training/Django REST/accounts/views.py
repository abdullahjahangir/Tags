from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from .serializers import SignUpSerializers


class SignupView(APIView):
    serializer_class = SignUpSerializers
    permission_classes = []

    def post(self, request: Request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "User Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# JWT Auth


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Successfully logged out."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Token Auth


class LoginTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            response = {
                "message": "Login Successfully",
                "token": token.key,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(
            data={"Message": "Invalid Credentials"}, status=status.HTTP_200_OK
        )

    def get(self, request, format=None):
        response_data = {
            "user": str(request.user),
            "token": str(request.auth),
        }
        return Response(data=response_data, status=status.HTTP_200_OK)


class LogoutTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
