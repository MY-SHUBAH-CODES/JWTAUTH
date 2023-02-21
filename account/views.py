from rest_framework.response import Response
from rest_framework import status
from rest_framework .views import APIView
from .serialzers import Userserializer,UseLoginSerializer
from django.contrib.auth import authenticate


class UserRegeitrationView(APIView):
    def post(self,request,format=None):
        serilizer=Userserializer(data=request.data)
        if serilizer.is_valid(raise_exception=True):
            user=serilizer.save()
            return Response({'msg':'registration success'},status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer=UseLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                return Response({'msg':"login successfully"})
            else:
                return Response({'msg':"bad req"})

                
