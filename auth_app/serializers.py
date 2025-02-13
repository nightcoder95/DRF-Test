from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    # Making the password write-only so it never gets sent back in a response.
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        
        return user

class UserSerializer(serializers.ModelSerializer):
    
    """
    This serializer convert User instances to JSON and validate updates.
    Only a subset of fields is exposed for security and simplicity.
    """
    class Meta:
        model = User
        # Only include safe fields. 
        fields = ('id', 'username')