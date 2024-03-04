from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilazers import *


@api_view(['GET'])
def filter_employee_username(request):
    username_id = request.GET.get('username')
    users = Employee.objects.filter(user_id=username_id).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_address(request):
    address = request.GET.get('address')
    users = Employee.objects.filter(address=address).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_profession(request):
    profession = request.GET.get('profession')
    users = Employee.objects.filter(profession=profession).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_rating(request):
    employee = Employee.objects.all().order_by('-rating')[:1]
    ser = EmployeeSer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_owner_name(request):
    owner_name = request.GET.get('owner_name')
    users = Order.objects.filter(owner_name=owner_name).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_address(request):
    address = request.GET.get('address')
    users = Order.objects.filter(address=address).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_admin(request):
    admin_id = request.GET.get('admin')
    users = Payment.objects.filter(admin_id=admin_id).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_order(request):
    order_id = request.GET.get('order')
    users = Payment.objects.filter(order_id=order_id).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_type(request):
    pyment_type = request.GET.get('pyment_type')
    users = Payment.objects.filter(pyment_type=pyment_type).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_employee(request):
    employee_id = request.GET.get('employee')
    users = Order.objects.filter(employee_id=employee_id).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_problem(request):
    problem = request.GET.get('problem')
    users = Order.objects.filter(problem=problem).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_service_cost(request):
    service_cost = request.GET.get('service_cost')
    users = Order.objects.filter(service_cost=service_cost).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)



