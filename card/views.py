from .models import Card, Exchange, Crypto, Currency
from .serializers import CardSerializer, ExchangeSerializer, CryptoSerializer, CurrencySerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class CurrencyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Currency
        fields = ['id', 'name']

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CurrencyFilter

    def create(self, request):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        instance = self.get_object()
        serializer = CurrencySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CryptoFilter(filters.FilterSet):
    nameKR = filters.CharFilter(lookup_expr='icontains')
    nameEN = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Crypto
        fields = ['id', 'nameKR', 'nameEN']

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

    @action(methods=["PUT"], detail=False, list=True)
    def add_currency(self, request, pk):
        instance = self.get_object()
        for i in request.data['currencies']:
            currency = Currency.objects.get(id=i)
            instance.exchanges.add(currency)
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(methods=["PUT"], detail=False, list=True)
    def add_currency(self, request, pk):
        instance = self.get_object()
        for i in request.data['cryptos']:
            crypto = Crypto.objects.get(id=i)
            instance.exchanges.add(crypto)
        return Response(status=status.HTTP_202_ACCEPTED)

class CardFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Card
        fields = ['id', 'name']

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
        crypto = Crypto.objects.get(id=request.data['crypto'])
        if serializer.is_valid():
            serializer.save(crypto=crypto)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["PUT"], detail=False, list=True)
    def add_exchange(self, request, pk):
        instance = self.get_object()
        for i in request.data['exchanges']:
            exchange = Exchange.objects.get(id=i)
            instance.exchanges.add(exchange)
        return Response(status=status.HTTP_202_ACCEPTED)