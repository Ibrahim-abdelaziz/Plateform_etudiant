# Generated by Django 2.2 on 2019-05-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0027_auto_20190520_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatpfe',
            name='filiere',
            field=models.CharField(choices=[('DUT-FC2', 'DUT-FC2'), ('DUT-GE2-EEI', 'DUT-GE2-EEI'), ('DUT-GE2-EII', 'DUT-GE2-EII'), ('DUT-GE2-RLI', 'DUT-GE2-RLI'), ('DUT-GEA2', 'DUT-GEA2'), ('DUT-GI2', 'DUT-GI2'), ('DUT-GM2', 'DUT-GM2'), ('DUT-TC2', 'DUT-TC2'), ('DUT-GP2', 'DUT-GP2')], max_length=100),
        ),
    ]
