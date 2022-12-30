from . import api
from rest_framework import routers
from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
router = routers.DefaultRouter()
router.register(r'pagos', api.PaymentSetView, 'todosCustom')
router.register(r'servicios', api.ServiceSetView, 'serviceCustom')



api_urlpatterns =[
    path('expirados',api.ExpiredPaymentSetView.as_view(),name='pagoexpCustom'),
    #path('servicios',api.ServiceSetView.as_view(),name='serviceCustom')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

api_urlpatterns += router.urls