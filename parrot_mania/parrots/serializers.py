from rest_framework import serializers

from parrots.models import Parrot


class ParrotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parrot
        fields = ('id', 'name', 'link')
