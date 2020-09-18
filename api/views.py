from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission, IsAdminUser

from api import models
from django.contrib.auth.models import Group, Permission

from api.authenticator import MyAuth


# class Demo(APIView):
    # authentication_classes = [BaseAuthentication]
    # def get(self,request,*args,**kwargs):
        # user = models.User.objects.first()
        # user2 = models.User.objects.first()
        # print(user2)
        # print(user.email)
        # print(user.user_permissions.first().name)

        # group = Group.objects.first()
        # print(group)
        # print(group.user_set.first().username)
        # print(group.permissions.first())

        # permission = Permission.objects.first()
        # print(permission.name)
        # print(permission.user_set.first().username)
        # per = Permission.objects.filter(pk=1).first()
        # print(per.group_set.first().name)
        # return Response("ok")

class Demo2(APIView):
    # permission_classes = [IsAdminUser]
    authentication_classes = [MyAuth]
    # throttle_classes = [UserRateThrottle]

    def get(self,request,*args,**kwargs):
        return Response("get")
    def post(self,request,*args,**kwargs):
        return Response("post")

