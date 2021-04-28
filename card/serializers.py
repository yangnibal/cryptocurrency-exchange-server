from .models import Card, Exchange, Crypto, Currency, CardGroup
from rest_framework import serializers

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name']

    def update(self, instance, validated_data, partial=True):
        instance.name = validated_data.get('name', instance.name)
        
        instance.save()
        return instance

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['id', 'name']

    def update(self, instance, validated_data, partial=True):
        instance.nameKR = validated_data.get('name', instance.name)

        instance.save()
        return instance

class ExchangeSerializer(serializers.ModelSerializer):
    currencies = CurrencySerializer(many=True)
    cryptos = CryptoSerializer(many=True)
    class Meta:
        model = Exchange
        fields = ['id', 'name', 'currencies', 'cryptos']

    def update(self, instance, validated_data, partial=True):
        instance.name = validated_data.get('name', instance.name)
        instance.currencies = validated_data.get('currencies', instance.currencies)
        instance.cryptos = validated_data.get('cryptos', instance.cryptos)

        instance.save()
        return instance

class CardGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardGroup
        fields = ['id', 'name']

class CardSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.name', read_only=True)
    exchanges = ExchangeSerializer(many=True, read_only=True)
    crypto = CryptoSerializer(read_only=True)

    class Meta:
        model = Card
        fields = ['id', 'name', 'owner', 'exchanges', 'crypto']

    def update(self, instance, validated_data, partial=True):
        instance.name = validated_data.get('name', instance.name)
        instance.exchanges = validated_data.get('exchanges', instance.exchanges)
        instance.crypto = validated_data.get('crypto', instance.crypto)

        instance.save()
        return instance


