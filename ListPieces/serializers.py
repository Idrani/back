from re import U
from rest_framework import serializers
from ListPieces.models import LIST_PIECES

class LISTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LIST_PIECES
        fields = ('id_piéce','NumOF', 'Qte','Ref','statut', 'Désignation', 'Matiére', 'Dimension', 'Qual',
        'Prévu_h', 'Réalisé_h', 'Conformité_C', 'Conformité_NC','Conf_C','NConf_C','Conf_NC','NConf_NC','Rest','avancement','id_plan', 'lien',)