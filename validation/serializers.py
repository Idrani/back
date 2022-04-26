from re import U
from rest_framework import serializers
from validation.models import VAL

class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VAL
        fields = ('NumOF','NumV', 'valide', 'date1', 'date2', 'date3', 'date4','date5')
