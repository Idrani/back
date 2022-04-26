from django.db import models

# Create your models here.
class LIST_PIECES(models.Model):
    id_piéce= models.AutoField(primary_key=True)
    NumOF = models.IntegerField(blank=False)
    Index = models.IntegerField(default=0)

    Qte = models.CharField(max_length=100,default="..")
    Désignation = models.CharField(max_length=100,default="..")
    Matiére = models.CharField(max_length=100,default="..")
    Dimension = models.CharField(max_length=100,default="..")
    Qual = models.CharField(max_length=100,default="..")
    Prévu_h = models.CharField(max_length=100,default="..")
    Réalisé_h = models.CharField(max_length=100,default="..")
    Conformité_C = models.CharField(max_length=100,default="..")
    Conformité_NC = models.CharField(max_length=100,default="..")
    
    # TotalCNC_Rea = models.CharField(max_length=100)
    # TotalCONV_Pre = models.IntegerField()
    # TotalCONV_Rea = models.IntegerField()
    # Conformite_C = models.IntegerField()
    # Conformite_NC = models.IntegerField()