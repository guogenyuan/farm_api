from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# from until.models import Common


class User(AbstractUser):
    ROLE_CHOICE = (("0", "客户"), ("1", "管理员"))
    SEX_CHOICE = (("0", "男"), ("1", "女"), ("2", "保密"))
    nickname = models.CharField(max_length=32, null=True)
    sex = models.CharField(choices=SEX_CHOICE, default="0", max_length=1, null=True)
    phone = models.CharField(max_length=11)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)
    role = models.CharField(choices=ROLE_CHOICE, max_length=1, default="0")
    # sales = models.ForeignKey('Sales', on_delete=models.CASCADE, null=True)


# class Sales(models.Model):
#     RANK_CHOICE = (("0", "销售员"), ("1", "销售经理"))
#     name = models.CharField(max_length=32)
#     rank = models.CharField(choices=RANK_CHOICE, default='0', max_length=1, verbose_name='职级')


class FarmCategory(models.Model):
    name = models.CharField(max_length=32)
    # image = models.ImageField(verbose_name='图片地址')


class FarmProduce(models.Model):
    UNIT_CHOICE = (('0', '两'), ('1', '斤'), ('2', '公斤'), ('3', '克'), ('4', '千克'), ('5', '吨'))
    name = models.CharField(max_length=32)
    productionDate = models.DateField(verbose_name='生产日期', null=True)
    expirationDate = models.DateField(verbose_name='有效期', null=True)
    numbers = models.IntegerField(verbose_name='数量', null=True)
    price = models.IntegerField(null=True, verbose_name='价格')
    unit = models.CharField(choices=UNIT_CHOICE, max_length=1, verbose_name="单位", null=True)
    # image = models.ImageField(verbose_name='图片地址')
    category = models.ForeignKey("FarmCategory", on_delete=models.CASCADE, null=True)


class Order(models.Model):
    STATE_CHOICE = (('0', '未付款'), ('1', '待发货'), ('2', '发货中'), ('3', '交易成功'), ('4', '退货中'), ('5', '退货成功'))
    orderNumber = models.IntegerField(unique=True, primary_key=True)
    createDate = models.DateField(verbose_name='创建日期', null=True)
    name = models.CharField(max_length=32)
    price = models.IntegerField(verbose_name='订单价格')
    state = models.CharField(choices=STATE_CHOICE, max_length=1, verbose_name='订单状态')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='客户')

