from .models import Card, Exchange, Crypto
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.name', read_only=True)
    exchange1 = serializers.CharField(source='exchange1.name')
    exchange2 = serializers.CharField(source='exchange2.name')
    class Meta:
        model = Card
        fields = ['id', 'name', 'owner', 'exchange1', 'exchange2']

    def update(self, instance, validated_data, partial=True):
        instance.name = validated_data.get('name', instance.name)
        instance.exchange1 = validated_data.get('exchange1', instance.exchange1)
        instance.exchange2 = validated_data.get('exchange2', instance.exchange2)

        instance.save()
        return instance


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
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
        instance.name = validated_data.gete('name', instance.name)

        instance.save()
        return instance