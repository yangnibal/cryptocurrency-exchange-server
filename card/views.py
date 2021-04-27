from .models import Card, Exchange, Crypto, Currency, CardGroup
from .serializers import CardSerializer, ExchangeSerializer, CryptoSerializer, CurrencySerializer, CardGroupSerializer
from .permissions import IsCardOwnerOrReadOnly
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

    @action(methods=['GET', 'PUT', 'DELETE'], detail=False, list=True)
    def currencies(self, request, pk):
        if request.method == 'GET':
            return get_currencies(request, pk)
        if request.method == 'PUT':
            return add_currencies(request, pk)
        if request.method == 'DELETE':
            return remove_currencies(request, pk)

    def get_currencies(self, request, pk):
        instance = self.get_object()
        serializer = ExchangeSerializer(instance)
        if serializer.is_valid():
            currencies = serializer.data['currencies']
            currency_serializer = CurrencySerializer(currencies, many=True)
            if currency_serializer.is_valid():
                return Response(currency_serializer.data, status=status.HTTP_200_OK)
            return Response(currency_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_currencies(self, request, pk):
        instance = self.get_object()
        for i in request.data['currencies']:
            currency = Currency.objects.get(id=i)
            instance.currencies.add(currency)
        return Response(status=status.HTTP_200_OK)

    def remove_currencies(self, request, pk):
        instance = self.get_object()
        for i in request.data['currencies']:
            currency = Currency.objects.get(id=i)
            instance.currencies.remove(currency)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET', 'PUT', 'DELETE'], detail=False, list=True)
    def cryptos(self, request, pk):
        if request.method == 'GET':
            return get_cryptos(request, pk)
        if request.method == 'PUT':
            return add_cryptos(request, pk)
        if request.method == 'DELETE':
            return remove_cryptos(request, pk)

    def get_cryptos(self, request, pk):
        instance = self.get_object()
        serializer = ExchangeSerializer(instance)
        if serializer.is_valid():
            cryptos = serializer.data['cryptos']
            crypto_serializer = CryptoSerializer(cryptos, many=True)
            if crypto_serializer.is_valid():
                return Response(crypto_serializer.data, status=status.HTTP_200_OK)
            return Response(crypto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_cryptos(self, request, pk):
        instance = self.get_object()
        for i in request.data['currencies']:
            crypto = Crypto.objects.get(id=i)
            instance.cryptos.remove(crypto)
        return Response(status=status.HTTP_200_OK)

    def remove_cryptos(self, request, pk):
        instance = self.get_object()
        for i in request.data['cryptos']:
            crypto = Crypto.objects.get(id=i)
            instance.cryptos.remove(crypto)
        return Response(status=status.HTTP_200_OK)

class CardGroupFilteer(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CardGroup
        fields = ['id', 'name']

class CardGroupViewset(viewsets.ModelViewSet):
    queryset = CardGroup.objects.all()
    serializer_class = CardGroupSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CardGroupFilteer



class CardFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Card
        fields = ['id', 'name']

    def create(self, request):
        serializer = CardGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        instance = self.get_object()
        serializer = CardGroupSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CardFilter
    permission_classes = [IsCardOwnerOrReadOnly]

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

    @action(methods=['GET', 'PUT', 'DELETE'], detail=False, list=True)
    def exchanges(self, request, pk):
        if request.method == 'GET':
            return get_exchanges(request, pk)
        if request.method == 'PUT':
            return add_exchanges(request, pk)
        if request.method == 'DELETE':
            return remove_exchanges(request, pk)

    def get_exchanges(self, request, pk):
        instance = self.get_object()
        serializer = CardSerializer(instance)
        if serializer.is_valid():
            exchanges = serializer.data['exchanges']
            exchange_serializer = ExchangeSerializer(cryptos, many=True)
            if exchange_serializer.is_valid():
                return Response(exchange_serializer.data, status=status.HTTP_200_OK)
            return Response(exchange_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_exchanges(self, request, pk):
        instance = self.get_object()
        for i in request.data['exchanges']:
            exchange = Exchange.objects.get(id=i)
            instance.exchanges.add(exchange)
        return Response(status=status.HTTP_200_OK)

    def remove_exchanges(self, request, pk):
        instance = self.get_object()
        for i in request.data['exchanges']:
            exchange = Exchange.objects.get(id=i)
            instance.exchanges.remove(exchange)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET', 'PUT', 'DELETE'], detail=False, list=True)
    def card_groups(self, request, pk):
        if request.method == 'GET':
            return get_card_groups(request, pk)
        if request.method == 'PUT':
            return add_card_groups(request, pk)
        if request.method == 'DELETE':
            return remove_card_groups(request, pk)

    def get_card_groups(self, request, pk):
        instance = self.get_object()
        serializer = CardSerializer(instance)
        if serializer.is_valid():
            card_groups = serializer.data['card_groups']
            card_group_serializer = CardGroupSerializer(card_groups, many=True)
            if card_group_serializer.is_valid():
                return Response(card_group_serializer.data, status=status.HTTP_200_OK)
            return Response(card_group_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_card_groups(self, request, pk):
        instance = self.get_object()
        for i in request.data['card_groups']:
            card_group = CardGroup.objects.get(id=i)
            instance.card_groups.add(card_group)
        return Response(status=status.HTTP_200_OK)

    def remove_card_groups(self, request, pk):
        instance = self.get_object()
        for i in request.data['card_groups']:
            card_group = CardGroup.objects.get(id=i)
            instance.card_groups.remove(card_group)
        return Response(status=status.HTTP_200_OK)