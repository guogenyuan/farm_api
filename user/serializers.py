from rest_framework import serializers

from user.models import User, Produce, Category, Order, ShoppingCart


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'sex', 'phone', 'address', 'email', 'role']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'sex', 'phone', 'address', 'email', 'role']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class FarmCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FarmProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Order
        fields = ['orderNumber', 'createDate', 'name', 'price', 'state', 'username']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ShoppingCartListSerializer(serializers.ModelSerializer):
    produceName = serializers.CharField(source='produce.name')
    producePrice = serializers.CharField(source='produce.price')
    produceNumber = serializers.IntegerField(source='produce.numbers')
    produceUnit = serializers.CharField(source='produce.unit')

    class Meta:
        model = ShoppingCart
        fields = ['produceName', 'producePrice', 'produceNumber', 'numbers', 'produceUnit', 'user']


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

