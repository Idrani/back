from django.db import models

# Create your models here.
class LIST_PIECES(models.Model):
    id_piéce= models.AutoField(primary_key=True)
    NumOF = models.IntegerField(blank=False)
    Index = models.IntegerField(default=0)

    Qte = models.CharField(max_length=100,default="..")
    Ref = models.CharField(max_length=100,default="..")
    statut = models.CharField(max_length=100,default="pas lancer")
    
    Désignation = models.CharField(max_length=100,default="..")
    Matiére = models.CharField(max_length=100,default="..")
    Dimension = models.CharField(max_length=100,default="..")
    Qual = models.CharField(max_length=100,default="..")
    Prévu_h = models.CharField(max_length=100,default="..")
    Réalisé_h = models.IntegerField(default=0)
    Conformité_C = models.CharField(max_length=100,default="..")
    Conformité_NC = models.CharField(max_length=100,default="..")
    
    # TotalCNC_Rea = models.CharField(max_length=100)
    # TotalCONV_Pre = models.IntegerField()
    # TotalCONV_Rea = models.IntegerField()
    Conf_C = models.IntegerField( blank=True, null=True)
    Conf_NC = models.IntegerField( blank=True, null=True)
    NConf_C = models.IntegerField( blank=True, null=True)
    NConf_NC = models.IntegerField( blank=True, null=True)
    Rest = models.IntegerField( blank=True, null=True)
    avancement = models.CharField(max_length=100,default="..")
