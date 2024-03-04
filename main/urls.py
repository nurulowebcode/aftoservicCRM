from django .urls import path
from .views import *


urlpatterns = [
    # ```````````````````````````` START EMPLOYEE ````````````````````````````````````````````````````````````````````
    path('filter-employee-user/', filter_employee_username),
    path('filter-employee-address/', filter_employee_address),
    path('filter-employee-profession/', filter_employee_profession),
    path('filter-employee-rating/', filter_employee_rating),

    # ```````````````````````````` START ORDER ````````````````````````````````````````````````````````````````````````
    path('filter-order-address/', filter_order_address),
    path('filter-order-owner-name/', filter_order_owner_name),
    path('filter-order-employee/', filter_order_employee),
    path('filter-order-problem/', filter_order_problem),
    path('filter-order-service-cost/', filter_order_service_cost),

    # ````````````````````````````````` START PAYMENT ``````````````````````````````````````````````````````````````````
    path('filter-payment-admin/', filter_payment_admin),
    path('filter-payment-order/', filter_payment_order),
    path('filter-payment-type/', filter_payment_type),

]
