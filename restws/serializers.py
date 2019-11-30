from rest_framework import serializers

from restws.models import Charger


class ChargerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charger
        fields = ['voltage', 'wireless', 'factory']

    def validate(self, attrs):
        if attrs['voltage'] > 220:
            raise serializers.ValidationError('Voltage exceeds 220 volts')
        return attrs
