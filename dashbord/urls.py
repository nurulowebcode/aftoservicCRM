from django .urls import path
from .views import *


urlpatterns = [
    # ~~~~~~~~~~~~~~~~~~~START-Employee~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    path('get-employee-items/', GetEmployeeItems.as_view()),
    path('create-employee-items/', CreateEmployeeAPiView.as_view()),
    path('update-employee-items/<int:pk>/', UpdateEmployeeAPiView.as_view()),
    path('delete-employee-items/<int:pk>/', DeleteEmployeeAPiView.as_view()),

    path('get-cassa/', GetCassaAPiView.as_view()),
    path('create-cassa/', CreateCassaAPiView.as_view()),
    path('update-cassa/<int:pk>/', UpdateCassaAPiView.as_view()),
    path('delete-cassa/<int:pk>/', DeleteCassaAPiView.as_view()),

    path('get-order/', GetOrderAPiView.as_view()),
    path('create-order/', CreateOrderAPiView.as_view()),
    path('update-order/<int:pk>/', UpdateOrderAPiView.as_view()),
    path('delete-order/<int:pk>/', DeleteOrderAPiView.as_view()),

    path('get-payment/', GetPaymentAPiView.as_view()),
    path('create-payment/', GetPaymentAPiView.as_view()),
    path('update-payment/<int:pk>/', GetPaymentAPiView.as_view()),
    path('delete-payment/<int:pk>/', GetPaymentAPiView.as_view()),

    path('get-comment/', GetCommentAPiView.as_view()),
    path('create-comment/', CreateCommentAPiView.as_view()),
    path('update-comment/<int:pk>/', UpdateCommentAPiView.as_view()),
    path('delete-comment/<int:pk>/', DeleteCommentAPiView.as_view()),

    path('get-garage/', GetGarageAPiView.as_view()),
    path('create-garage/', CreateGarageAPiView.as_view()),
    path('update-garage/<int:pk>/', UpdateGarageAPiView.as_view()),
    path('delete-garage/<int:pk>/', DeleteGarageAPiView.as_view()),


]

