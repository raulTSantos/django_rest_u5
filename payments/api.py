from rest_framework import serializers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters 
from rest_framework import permissions

from .models import Pagos
from .serializers import PagoSerializer
from .paginations import StandardResultsSetPagination

class PaymentSetView(viewsets.ModelViewSet):
    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer
    #pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ['user__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'