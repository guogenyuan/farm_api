from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User, FarmProduce, FarmCategory
from user.serializers import ListUserSerializer, UserSerializer, FarmProduceSerializer, FarmCategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role']
    # http_method_names = ['head', 'option', 'get', 'post', 'patch']

    def get_serializer_class(self):
        _serializer_class = self.serializer_class
        if self.action == "list":
            _serializer_class = ListUserSerializer
        else:
            _serializer_class = UserSerializer
        return _serializer_class

    @action(methods=['POST'], detail=False, permission_classes=[])
    def login(self, request):
        _username = request.data['username']
        _password = request.data['password']
        user = authenticate(username=_username, password=_password)
        # user = User.objects.filter(username=_username)
        # if not user.exists():
        #     return Response("用户不存在！")
        # print(user.first().password)
        # if user.first().password != _password:
        #     return Response("密码错误！")
        login(request, user)
        return Response("登录成功")

    @action(methods=['POST'], detail=False, permission_classes=[])
    def logout(self, request):
        logout(request)
        return Response("注销成功")


class FarmCategoryViewSet(viewsets.ModelViewSet):
    queryset = FarmCategory.objects.all()
    serializer_class = FarmCategorySerializer


class FarmProduceViewSet(viewsets.ModelViewSet):
    queryset = FarmProduce.objects.all()
    serializer_class = FarmProduceSerializer



