from rest_framework import serializers
from .models import mnb_deviza, mnb_name

class MnbSerializer(serializers.ModelSerializer):
    class Meta:
        model = mnb_deviza
        fields="__all__"

class MnbNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = mnb_name
        fields="__all__"