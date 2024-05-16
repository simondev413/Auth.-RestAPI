from django.urls import path,include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .viewsets import RoleViews, UserViews,PermissionsViews,RoloPermissionViews, UserRoleViews,SessionViews, VerificationCodeViews

app_name = 'API'

router = DefaultRouter()
router.register(r'users',UserViews,basename='usuarios')
router.register(r'roles',RoleViews,basename='roles')
router.register(r'permissions',PermissionsViews,basename='permissoes')
router.register(r'role_permissions',RoloPermissionViews,basename='role_permissions')
router.register(r'user_roles',UserRoleViews,basename='user_roles')
router.register(r'sessions',SessionViews,basename='sessions')
router.register(r'verification_codes',VerificationCodeViews,basename='verification_codes')

urlpatterns = [
  path('/', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]