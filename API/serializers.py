from django.db.models import fields
from rest_framework import serializers
from .models import User,Role, Permission, RolePermission, UserRole, Session,VerificationCode

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    #extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User(
        email=validated_data['email'],
        username=validated_data['username']
  )
    user.set_password(validated_data['password'])
    user.save()
    return user

class RoleSerrializer(serializers.ModelSerializer):
  class Meta:
    model = Role
    fields = '__all__'

class PermissionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Permission
    fields = '__all__'

class RolePermissonSerializer(serializers.ModelSerializer):
  class Meta:
    model = RolePermission
    fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserRole
    fields = '__all__'
  

class SesionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Session
    fields = '__all__'

class VerificationCodeSerializer(serializers.Serializer):
  class Meta:
    model = VerificationCode
    fields = '__all__'