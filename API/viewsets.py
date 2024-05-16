from .serializers import UserRoleSerializer, UserSerializer,RoleSerrializer,PermissionsSerializer,RolePermissonSerializer,UserSerializer,SesionSerializer, VerificationCodeSerializer
from .models import User,Role, Permission, RolePermission, UserRole, Session, VerificationCode

from rest_framework import serializers, viewsets


class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViews(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerrializer

class PermissionsViews(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionsSerializer

class RoloPermissionViews(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissonSerializer

class UserRoleViews(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class SessionViews(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SesionSerializer

class VerificationCodeViews(viewsets.ModelViewSet):
    queryset = VerificationCode.objects.all()
    serializer_class = VerificationCodeSerializer