# from django.contrib import messages, auth
# from django.shortcuts import render, redirect, HttpResponse
# from .form import UserForm, BaseForm
# from .models import BaseUser
# from django.contrib.auth.models import User
#
# # Create your views here.
# def home(requests):
#     form = UserForm
#     baseform = BaseForm
#     if requests.method == 'POST':
#         username = requests.POST['username']
#         email = requests.POST['email']
#         password1 = requests.POST['password1']
#         password2 = requests.POST['password2']
#         phone_number = requests.POST['phone_number']
#
#
#         if len(password1) >= 8 and password1 == password2:
#             if len(phone_number) < 11 or len(phone_number) > 15:
#
#                 return HttpResponse('enter the correct phone number')
#             else:
#                 try:
#                     user = User.objects.get(username= username)
#                     return HttpResponse('user already exist')
#                 except User.DoesNotExist:
#                     reuser = User.objects.create_user(username=username, email=username, password = password1)
#                     phone_number = requests.POST['phone_number']
#                     user_type = requests.POST['user_type']
#                     if user_type == '':
#                         user_type == 'patient'
#
#
#                     BaseUser.objects.create(user_type = user_type, user = reuser, phone_number = phone_number )
#                     auth.login(requests, reuser)
#                     return HttpResponse('sign up successfully')
#         else:
#             messages.success(requests, "place make sure your password is up 8 mixed value")
#             context = {'form': form,
#                        'baseform': baseform}
#             return render(requests, 'hospital/home.html', context)
#         # form = UserForm(requests.POST)
#         # baseform = BaseForm(requests.POST, instance=requests.user.baseuser)
#         # if form.is_valid() and baseform.is_valid():
#         #     user = form.save()
#         #     baseform = baseform.save(commit=False)
#         #     baseform.user = user
#         #     baseform.save()
#         #     return HttpResponse('successful sign up')
#
#
#
#     context = {'form': form,
#                'baseform':baseform}
#     return render(requests, 'hospital/home.html', context)
import jwt
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, LoginSerializer, AppointmentSerializer
from django.contrib import auth
from django.conf import settings

from .models import User

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class RegisterView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class AppointmentView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AppointmentSerializer

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
