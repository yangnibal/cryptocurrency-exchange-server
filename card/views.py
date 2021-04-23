from .models import Card, Exchange, Crypto
from .serializers import CardSerializer, ExchangeSerializer, CryptoSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class CryptoFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Crypto
        fields = ['id', 'name']

class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CryptoFilter

    def create(self, request):
        serializer = CryptoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        instance = self.get_object()
        serializer = CryptoSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExchangeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Exchange
        fields = ['id', 'name']

class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ExchangeFilter

    def create(self, request):
        serializer = ExchangeSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        instance = self.get_object()
        serializer = ExchangeSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    exchange1 = filters.CharFilter(field_name='name', lookup_expr='icontains')
    exchange2 = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['id', 'name', 'exchange1', 'exchange2']

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CardFilter

    def create(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        instance = self.get_object()
        serializer = CardSerializer(instance, data=request.data)
        exchange1 = Exchange.objects.get(name=request.data['exchange1'])
        exchange2 = Exchange.objects.get(name=request.data['exchange2'])
        if serializer.is_valid():
            serializer.save(exchange1=exchange1, exchange2=exchange2)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)