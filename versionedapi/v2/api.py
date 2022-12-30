from rest_framework import serializers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters 
from rest_framework import permissions
from rest_framework import parsers

from versionedapi.models import Payment_user,Expired_payments,Services
from .serializers import PaymentSerializer,ExpiredPaymentSerializer,ServiceSerializer
from .pagination import StandardResultsSetPagination,SimplePagination

class PaymentSetView(viewsets.ModelViewSet):
    #queryset = Payment_user.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]

    search_fields = [ 'paymentDate', 'expirationDate']
    throttle_scope = 'pagos'
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
             return Payment_user.objects.all()

        return Payment_user.objects.filter(user=user.id)

    def get_permissions(self):
        # Allow only by explicit exception
        if self.action == 'retrieve' or self.action == 'list' or self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        # Overrides to tightest security: Only superuser can create, update, partial update, destroy, list
        else:
            self.permission_classes = [permissions.IsAdminUser]

        return super().get_permissions()

class ExpiredPaymentSetView(generics.ListCreateAPIView):
    #queryset = Expired_payments.objects.all()
    serializer_class = ExpiredPaymentSerializer
    
    pagination_class = StandardResultsSetPagination
    throttle_scope = 'others'

    def get_queryset(self):
        user = self.request.user
        payments= Payment_user.objects.filter(user=user.id)
        if user.is_superuser and user.is_staff:
             return Expired_payments.objects.all()
        
        return Expired_payments.objects.filter( payment_user_id__in=payments)
    

    
class ServiceSetView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = [permissions.AllowAny]
    throttle_scope = 'others'
    pagination_class = SimplePagination
    

    def get_permissions(self):
        # Allow only by explicit exception
        if self.action == 'retrieve' or self.action == 'list':
            self.permission_classes = [permissions.IsAuthenticated]
        # Overrides to tightest security: Only superuser can create, update, partial update, destroy, list
        else:
            self.permission_classes = [permissions.IsAdminUser]

        return super().get_permissions()