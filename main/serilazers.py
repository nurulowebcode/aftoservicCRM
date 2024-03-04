from rest_framework import serializers
from .models import *


class UserSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = "__all__"


class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employee
        fields = "__all__"


class CassaSer(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"


class OrderSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Order
        fields = "__all__"


class PaymentSer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Payment
        fields = "__all__"


class CommentSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Comment
        fields = "__all__"


class GarageSer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = "__all__"








