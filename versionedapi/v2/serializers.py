from rest_framework import serializers
from versionedapi.models import Payment_user,Services,Expired_payments
from django.utils import timezone
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        read_only_fields = "paymentDate",
    def create(self, validated_data):
        #pay_date = validated_data.pop('paymentDate')
        pay_date = timezone.now().date()
        print("pay-date:",pay_date)
        exp_date = validated_data.pop('expirationDate')
        amount_x= validated_data.pop('amount')
        print("ex:",pay_date)
        
        print( pay_date >exp_date)
        if pay_date >exp_date:
            p_instance = Payment_user.objects.create(**validated_data, paymentDate=pay_date,expirationDate=exp_date,amount=float(amount_x)+40.0)
            Expired_payments.objects.create(payment_user=p_instance)
        else:
            p_instance = Payment_user.objects.create(**validated_data, paymentDate=pay_date,expirationDate=exp_date,amount=float(amount_x))
        return p_instance



class ExpiredPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = '__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'