from re import U
from rest_framework import serializers
from followUP.models import OF

class OFSerializer(serializers.ModelSerializer):
    class Meta:
        model = OF
        fields = ('RefPr','NomPr', 'StatutPr', 'NumOF', 'Priorité' ,'Realise_T','Rest_T','Avancement','State','cloture')
        