from rest_framework import serializers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters 
from rest_framework import permissions

from versionedapi.models import Payment_user,Expired_payments,Services
from .serializers import PaymentSerializer,ExpiredPaymentSerializer,ServiceSerializer
#from .pagination import StandardResultsSetPagination

class PaymentSetView(viewsets.ModelViewSet):
    queryset = Payment_user.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    #pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]

    search_fields = [ 'paymentDate', 'expirationDate']
    throttle_scope = 'pagos'

class ExpiredPaymentSetView(generics.ListCreateAPIView):
    queryset = Expired_payments.objects.all()
    serializer_class = ExpiredPaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = 'others'

""" class ServiceSetView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = 'others' """
    
class ServiceSetView(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = 'others'