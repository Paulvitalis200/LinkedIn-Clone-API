from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ('id', 'first_name', 'last_name', 'password', 'email', 'country', 'city', 'job_title', 'company', 'verified')