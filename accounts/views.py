from django.core.mail import send_mail
from django.contrib.auth.models import User

from accounts.models import Property
from .serializers import RegisterSerializer, ResetPasswordSerializer , UserProfileSerializer,PropertySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import *
from rest_framework import viewsets

from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            # Implémenter l'envoi d'email avec un lien de réinitialisation ici
            send_mail(
                'Password Reset Request',
                'Use this link to reset your password...',
                'no-reply@myapp.com',
                [email],
                fail_silently=False,
            )
            return Response({"message": "Reset email sent"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# Vue pour lister les logements et obtenir les détails d’un logement

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # Requêtes GET pour lister les logements et obtenir les détails d'un logement
    def list(self, request):
        properties = self.get_queryset()
        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        property = self.get_object()
        serializer = self.get_serializer(property)
        return Response(serializer.data)