# Generated by Django 2.2.12 on 2022-05-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LIST_PIECES',
            fields=[
                ('id_piéce', models.AutoField(primary_key=True, serialize=False)),
                ('NumOF', models.IntegerField()),
                ('Index', models.IntegerField(default=0)),
                ('Qte', models.CharField(default='..', max_length=100)),
                ('Ref', models.CharField(default='..', max_length=100)),
                ('statut', models.CharField(default='pas lancer', max_length=100)),
                ('Désignation', models.CharField(default='..', max_length=100)),
                ('Matiére', models.CharField(default='..', max_length=100)),
                ('Dimension', models.CharField(default='..', max_length=100)),
                ('Qual', models.CharField(default='..', max_length=100)),
                ('Prévu_h', models.CharField(default='..', max_length=100)),
                ('Réalisé_h', models.IntegerField(default=0)),
                ('Conformité_C', models.CharField(default='..', max_length=100)),
                ('Conformité_NC', models.CharField(default='..', max_length=100)),
            ],
        ),
    ]
