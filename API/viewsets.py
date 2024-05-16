from .serializers import UserRoleSerializer, UserSerializer,RoleSerrializer,PermissionsSerializer,RolePermissonSerializer,UserSerializer,SesionSerializer, VerificationCodeSerializer
from .models import User,Role, Permission, RolePermission, UserRole, Session, VerificationCode

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def logout(self, request, pk=None):
            # Implementação de logout
            request.auth.delete()
            return Response({'detail': 'Logged out successfully'}, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def verify_email(self, request):
        email = request.data.get('email')
        code = request.data.get('verificationCode')
        user = User.objects.filter(email=email).first()
        if user:
            verification_code = VerificationCode.objects.filter(user=user, code=code).first()
            if verification_code and verification_code.expires_at > timezone.now():
                user.is_email_verified = True
                user.save()
                return Response({'detail': 'Email verified successfully'}, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid or expired verification code'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def recover_password(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            code = VerificationCode.objects.create(user=user, code='123456', expires_at=timezone.now() + timedelta(minutes=10))
            send_mail(
                'Password Recovery',
                f'Your verification code is {code.code}',
                'from@example.com',
                [email],
            )
            return Response({'detail': 'Password recovery email sent'}, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


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