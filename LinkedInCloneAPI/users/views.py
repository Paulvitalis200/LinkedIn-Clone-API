from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from users.models import User
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        users = User.objects.all()

        first_name = request.GET.get('first_name', None)
        if first_name is not None:
            users = users.filter(first_name__icontains=first_name)
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)