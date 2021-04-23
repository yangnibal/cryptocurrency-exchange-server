from .models import Card, Exchange, Crypto
from rest_framework import serializers

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ['id', 'nameKR', 'nameEN']

    def update(self, instance, validated_data, partial=True):
        instance.nameKR = validated_data.get('nameKR', instance.nameKR)
        instance.nameEN = validated_data.get('nameEN', instance.nameEN)

        instance.save()
        return instance

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['id', 'nameKR', 'nameEN']

    def update(self, instance, validated_data, partial=True):
        instance.nameKR = validated_data.get('nameKR', instance.nameKR)
        instance.nameEN = validated_data.get('nameEN', instance.nameEN)

        instance.save()
        return instance

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


