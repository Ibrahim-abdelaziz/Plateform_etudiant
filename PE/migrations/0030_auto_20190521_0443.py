# Generated by Django 2.2 on 2019-05-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0029_auto_20190521_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatpfe',
            name='filiere',
            field=models.CharField(choices=[('DUT-FC2', 'DUT-FC2'), ('DUT-GE2-EEI', 'DUT-GE2-EEI'), ('DUT-GE2-EII', 'DUT-GE2-EII'), ('DUT-GE2-RLI', 'DUT-GE2-RLI'), ('DUT-GEA2', 'DUT-GEA2'), ('DUT-GI2', 'DUT-GI2'), ('DUT-GM2', 'DUT-GM2'), ('DUT-TC2', 'DUT-TC2'), ('DUT-GP2', 'DUT-GP2')], max_length=100),
        ),
    ]
