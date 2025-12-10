from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User

class RegisterView(APIView):
    def post(self, request):
        data = request.data

        user = User.objects.create(
            username=data["username"],
            email=data["email"],
            institucion=data.get("institucion", "institucion_1"),
            password=make_password(data["password"])
        )

        return Response({"message": "Usuario registrado", "id": user.id})

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Credenciales inválidas"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "user_id": user.id})
