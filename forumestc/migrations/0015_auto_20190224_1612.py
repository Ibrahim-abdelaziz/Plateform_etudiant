# Generated by Django 2.1.5 on 2019-02-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0014_auto_20190224_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(default='nom', max_length=15),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(default='prenom', max_length=15),
        ),
    ]
