from rest_framework import serializers
from rest_framework.exceptions import ValidationError, ParseError
from .models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

    def validate_balance(self, value):
        if 0 > value:
            raise ValidationError("Can't set a negative value for balance.")
        return value


class AccountTransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['balance']

    def validate(self, attrs):
        if not attrs:
            raise ValidationError("Type a value for balance")
        return attrs

    def validate_balance(self, value):
        if not value:
            raise ValidationError("Balance value for this operation can't be zero.")

        if 0 > value and abs(value) > self.instance.balance:
            raise ValidationError("Insufficient balance")

        return value
