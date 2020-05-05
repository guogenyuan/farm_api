from rest_framework import serializers

from user.models import User, FarmProduce, FarmCategory


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'nickname', 'sex', 'phone', 'address', 'email', 'role']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'nickname', 'sex', 'phone', 'address', 'email', 'role']


class FarmCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmCategory
        fields = '__all__'


class FarmProduceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmProduce
        fields = '__all__'
