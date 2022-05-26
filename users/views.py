from django.shortcuts import render

# Create your views here.
from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser



# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        name = request.data['name']


        user = User.objects.filter(email=email).first()
        user = User.objects.filter(name=name).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        # return Response ({
        #     'message' :'success'
        # })

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
                raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
        return Response(token)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


def UsersApi(request,id=0):
    if request.method=='GET':
        listpie = User.objects.all()
        list_serializer = UserSerializer(listpie, many=True)
        return JsonResponse(list_serializer.data, safe=False)

    elif request.method=='POST':
        list_data=JSONParser().parse(request)
        list_serializer = UserSerializer(data=list_data)
        if list_serializer.is_valid():
            list_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PATCH':
        list_data = JSONParser().parse(request)
        listpieces=User.objects.get(name=list_data['name'])
        list_serializer=UserSerializer(listpieces,data=list_data)
        if list_serializer.is_valid():
            list_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)        