# Generated by Django 2.1.5 on 2019-03-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0021_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evenement',
            name='created',
        ),
        migrations.AlterField(
            model_name='evenement',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
