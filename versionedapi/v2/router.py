from . import api
from rest_framework import routers
from django.urls import path
from django.urls import re_path

router = routers.DefaultRouter()
router.register(r'pagos', api.PaymentSetView, 'todosCustom')
router.register(r'servicios', api.ServiceSetView, 'serviceCustom')



api_urlpatterns =[
    path('expirados',api.ExpiredPaymentSetView.as_view(),name='pagoexpCustom'),
    #path('servicios',api.ServiceSetView.as_view(),name='serviceCustom')
]

api_urlpatterns += router.urls