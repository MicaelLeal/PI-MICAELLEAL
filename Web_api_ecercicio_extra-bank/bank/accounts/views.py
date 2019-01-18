from decimal import Decimal

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer, AccountTransactionsSerializer


@api_view(['GET', 'POST'])
def account_list(request):

    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def account_detail(request, account_id):

    try:
        account = Account.objects.get(id=account_id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data={"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = AccountTransactionsSerializer(account, request.data, partial=True)
        if serializer.is_valid():
            balance = Decimal(request.data['balance'])
            if balance > 0:
                account.credit(balance)
            else:
                account.debit(abs(balance))
            account.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(data={"errors": serializer.errors}, status=status.HTTP_409_CONFLICT)

    if request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
