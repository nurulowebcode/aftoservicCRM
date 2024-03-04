from main.models import User
from main.serilazers import UserSer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from .tokens import *

# -----------------------------------------------------USER_LOGIN---------------------------------------------------------------------
@api_view(['POST'])
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                token = get_tokens_for_user(usr)
                status = 200
                date = {
                    'status': status,
                    'username': username,
                    'token': token
                }
            else:
                status = 403
                message = "Invalid Password or Username"
                date = {
                    'status': status,
                    'message': message
                }
        except User.Doesnotexist:
            status = 404
            message = "this User is not defined"
            date = {
                'status': status,
                'message': message
            }
        return Response(date)
    except Exception as err:
        return Response(f'{err}')
#-----------------------------------------------------USER_SANG-UP---------------------------------------------------------------------

@api_view(['POST'])
def sang_up_view(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        new = User.objects.create_user(
            username=username,
            password=password,
            address=address,
            phone_number=phone_number,
        )
        ser = UserSer(new)
        return Response(ser.data)
    except Exception as err:
        return Response(f'{err}')

#-----------------------------------------------------USER_LOGOUT---------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'date': 'sucses'})




# -----------------------------------------------------USER_EDITE---------------------------------------------------------------------
@api_view(['PUT'])
def edit_user_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.POST.get('username')
            password = request.GET.get('password')
            user.username = username
            if password is not None:
                user.set_password(password)
                user.save()
                ser = UserSer(user)
                return Response(ser.data)
        except:
            status = 404
            message = "Request failed"
            date = {
                'status': status,
                'message': message
            }
    except:
        status = 404
        message = "User not found"
        date = {
            'status': status,
            'message': message
        }
        return Response(date)

#---------------------------------------------USER_delete-----------------------------------------------------------------------------------------

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        date = {
            'message': "User deleted successfully"
        }
    except:
        status = 404
        message = "User nod found"
        date = {
            'status': status,
            'message': message
        }
    return Response(date)









