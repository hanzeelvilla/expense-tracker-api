from rest_framework.decorators import api_view, authentication_classes, permission_classes #function based views
from rest_framework.response import Response #response with JSON and status codes
from rest_framework import status #create status codes

from django.shortcuts import get_object_or_404 #checks if the user exists
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    #Serialize the data so it can be in the db
    serializer = UserSerializer(data=request.data) #What data? the requested data
    if serializer.is_valid():
        serializer.save()#Save the data in the db if is valid
        user = User.objects.get(username=request.data["username"]) #get the user
        user.set_password(request.data["password"]) #hash the pswd
        user.save() #save the changes
        token, created = Token.objects.create(user=user) #get user token
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #return why the serializer failed

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def login(request):
    user = get_object_or_404(User, username=request.data["username"]) #user model and requested user
    if not user.check_password(request.data["password"]): #Compares pswd
        return Response({"detail": "No User matches the given query."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(["POST"])
def logout(request):
    request.auth.delete()
    return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
