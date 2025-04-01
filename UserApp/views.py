from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, UpdateUserPasswordSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
# from permissions import IsAuthorOrReadOnly
from .throttles import CustomRateThrottle

class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email, password=password).first()
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)






class UserIdAPI(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUserPasswordAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = UpdateUserPasswordSerializer
    def put(self, request):
        username = request.data.get('username')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if User.objects.all().filter(username=username,password=old_password).exists():
            User.objects.filter(username=username).update(password=new_password)
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

class ListUsersAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class AllUsersAPI(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


# class DeleteUserAPI(APIView):
#     def delete(self,request, id):
#         try:
#             queryset = User.objects.get(id=id)
#             queryset.delete()
#             return Response({"message":"user  delete succesfully"}, status=204)
#         except User.DoesNotExist:
#             return Response({"error":"User not found"}, status=404)

class DeleteUserAPI(APIView):
    permission_classes = [IsAuthenticated,]
    # throttle_classes = [CustomRateThrottle]

    def delete(self, request, id):
        queryset = User.objects.filter(id=id).first()
        if not queryset:
            return Response({"error":"User not found"},status=404)
        queryset.delete()
        return Response({"message":f"User deleted succesfully: {id}"},status=200)
