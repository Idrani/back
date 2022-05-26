from django.db import models

# Create your models here.
class OF(models.Model):
    NumOF = models.IntegerField(primary_key=True)
    NomPr = models.CharField(default="..", max_length=100)
    StatutPr = models.CharField(default="..", max_length=100)
    RefPr = models.IntegerField( blank=True, null=True)
    Priorité = models.CharField(default="..", max_length=100)
    Realise_T=models.IntegerField( blank=True, null=True)
    Rest_T=models.IntegerField( blank=True, null=True)
    Avancement=models.CharField(default="..", max_length=100)
    State=models.CharField(default="..", max_length=100)


    # PA_FAO = models.IntegerField(max_length=100)
    # PA_CNC = models.IntegerField(max_length=100)
    # PA_Router = models.IntegerField(max_length=100)
    # PA_Frai = models.IntegerField(max_length=100)
    # PA_Tournage = models.IntegerField(max_length=100)
    # PA_Eb = models.IntegerField(max_length=100)
    # PA_alu = models.IntegerField(max_length=100)
    # PA_alu = models.IntegerField(max_length=100)
    # C_NP_NC = models.IntegerField(max_length=100)
    # C_NP_C = models.IntegerField(max_length=100)
    # NH_FAO_PR = models.IntegerField(max_length=100)
    # NH_FAO_RE = models.IntegerField(max_length=100)
    # NH_CNC_PR = models.IntegerField(max_length=100)
    # NH_CNC_RE = models.IntegerField(max_length=100)
    # NH_CON_PR = models.IntegerField(max_length=100)
    # NH_CON_RE = models.IntegerField(max_length=100)
    # NH_EB_PR = models.IntegerField(max_length=100)
    # NH_EB_RE = models.IntegerField(max_length=100)
    # DD_PR = models.DateField()
    # DD_RE = models.DateField()
    # DC_PR = models.DateField()
    # DC_PRA = models.DateField()
    # DC_RE = models.DateField()
    # Ecart_Livraison = models.IntegerField(max_length=100)
    # PA_global = models.IntegerField(max_length=100)
    # PA_global = models.IntegerField(max_length=100)
    # Commenatire = models.CharField(max_length=100)
