from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from main.models import *
from main.serilazers import *


"""```````````````````````````````````START-EMPLOYEE``````````````````````````````````````````````````````````````````"""
class GetEmployeeItems(ListCreateAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer



class CreateEmployeeAPiView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


class UpdateEmployeeAPiView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


class DeleteEmployeeAPiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer

"""```````````````````````````````````START-CASSA``````````````````````````````````````````````````````````````````"""
class GetCassaAPiView(ListCreateAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSer


class CreateCassaAPiView(CreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


class UpdateCassaAPiView(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


class DeleteCassaAPiView(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


"""```````````````````````````````````START-ORDER``````````````````````````````````````````````````````````````````"""
class GetOrderAPiView(ListCreateAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSer


class CreateOrderAPiView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSer


class UpdateOrderAPiView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSer


class DeleteOrderAPiView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSer

"""```````````````````````````````````START-PAYMENT``````````````````````````````````````````````````````````````````"""
class GetPaymentAPiView(ListCreateAPIView):
    queryset = Payment.objects.all().order_by('-id')
    serializer_class = PaymentSer


class CreatePaymentAPiView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer


class UpdatePaymentAPiView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer


class DeletePaymentAPiView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer


"""```````````````````````````````````START-COMMENT``````````````````````````````````````````````````````````````````"""
class GetCommentAPiView(ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSer


class CreateCommentAPiView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


class UpdateCommentAPiView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


class DeleteCommentAPiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer



"""```````````````````````````````````START-GARAGE``````````````````````````````````````````````````````````````````"""
class GetGarageAPiView(ListCreateAPIView):
    queryset = Garage.objects.all().order_by('-id')
    serializer_class = GarageSer

class CreateGarageAPiView(CreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSer


class UpdateGarageAPiView(UpdateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSer


class DeleteGarageAPiView(DestroyAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSer

