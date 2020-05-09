from rest_framework import serializers

from user.models import User, FarmProduce, FarmCategory, Order


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'sex', 'phone', 'address', 'email', 'role']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'sex', 'phone', 'address', 'email', 'role']


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
        model = FarmCategory
        fields = '__all__'


class FarmProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmProduce
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderNumber', 'createDate', 'name', 'price', 'state']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

