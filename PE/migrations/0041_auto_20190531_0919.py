# Generated by Django 2.2 on 2019-05-31 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0040_laurea_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laurea',
            name='filiere_actual',
        ),
        migrations.RemoveField(
            model_name='laurea',
            name='ville',
        ),
    ]
