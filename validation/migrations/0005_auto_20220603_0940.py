# Generated by Django 2.2.12 on 2022-06-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0004_val_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='val',
            old_name='owner',
            new_name='owner1',
        ),
        migrations.AddField(
            model_name='val',
            name='owner2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='val',
            name='owner3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='val',
            name='owner4',
            field=models.CharField(default='', max_length=100),
        ),
    ]
