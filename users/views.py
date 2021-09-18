from django.shortcuts import render
from rest_framework import generics, permissions

from users.models import Account
from users.permissions import IsOwner
from users.serializers import AccountRegistrationSerializer, AccountDetailSerializer


class AccountRegisterAPIView(generics.CreateAPIView):
    """
    This endpoint registers users based on the fields
    """
    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny,)


class AccountDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AccountDetailSerializer
    queryset = Account.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)


