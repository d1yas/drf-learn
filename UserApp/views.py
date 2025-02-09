from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


# Create your views here.


class AllUsersAPI(APIView):
    def get(self, request):
        people = User.objects.all()
        serializer = UserSerializer(people, many=True)
        return Response(serializer.data)



class UserIdAPI(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
