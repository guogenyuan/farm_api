from django.contrib.auth import authenticate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user.models import User, Produce, Category, Order, ShoppingCart
from user.serializers import ListUserSerializer, UserSerializer, FarmProduceSerializer, FarmCategorySerializer, \
    OrderSerializer, UserRegisterSerializer, OrderListSerializer, ShoppingCartSerializer
from user.utils import IsNotAdminsUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role']
    http_method_names = ['head', 'option', 'get', 'post', 'patch']

    def get_serializer_class(self):
        _serializer_class = self.serializer_class
        if self.action == "list":
            _serializer_class = ListUserSerializer
        elif self.action == 'create':
            _serializer_class = UserRegisterSerializer
        else:
            _serializer_class = UserSerializer
        return _serializer_class

    def get_permissions(self):
        if self.action in ["create", 'login']:
            return []
        elif self.action == 'list':
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        _username = request.data['username']
        _password = request.data['password']
        if User.objects.filter(username=_username).exists():
            return Response(data={'code': 1001, 'data': '用户已存在'})
        super().create(request, *args, **kwargs)
        return Response(data={'code': 200, 'data': '注册成功'})

    @action(methods=['POST'], detail=False, permission_classes=[])
    def login(self, request):
        _username = request.data['username']
        _password = request.data['password']

        _user = User.objects.filter(username=_username)
        if not _user.exists():
            return Response(data={'code': 1001, 'data': '用户不存在'})
        user = authenticate(username=_username, password=_password)
        # 创建token
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'code': 200, 'data': "登录成功", 'token': token.key, 'user': UserSerializer(user).data},
                        headers={'Authorization': f"Token {token.key}"})

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request):
        Token.objects.get(user=request.user).delete()
        return Response(data={'code': 200, 'data': "注销成功"})

    @action(methods=["GET"], detail=False, permission_classes=[IsAuthenticated])
    def token_user(self, request):
        user = User.objects.get(id=request.user.id)
        return Response(data={'code': 200, 'data': UserSerializer(user).data})


class FarmCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = FarmCategorySerializer

    def get_permissions(self):
        if self.action == 'list':
            return []
        else:
            return [IsAdminUser()]


class FarmProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = FarmProduceSerializer

    def get_permissions(self):
        if self.action == 'list':
            return []
        else:
            return [IsAdminUser()]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        _serializer_class = self.serializer_class
        if self.action == "list":
            _serializer_class = OrderListSerializer
        else:
            _serializer_class = OrderSerializer
        return _serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [IsNotAdminsUser()]
        else:
            return [IsAuthenticated()]


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = [IsAuthenticated]

