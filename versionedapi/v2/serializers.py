from rest_framework import serializers
from versionedapi.models import Payment_user,Services,Expired_payments

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        #read_only_fields = "paymentDate",
    def create(self, validated_data):
        pay_date = validated_data.pop('paymentDate')
        print("pay:",pay_date)
        exp_date = validated_data.pop('expirationDate')
        print("ex:",pay_date)
        p_instance = Payment_user.objects.create(**validated_data, paymentDate=pay_date,expirationDate=exp_date)
        print( pay_date >exp_date)
        if pay_date >exp_date:
            print(p_instance.id)
            Expired_payments.objects.create(payment_user=p_instance)
        return p_instance



class ExpiredPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = '__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'