# Generated by Django 2.1.5 on 2019-02-10 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0005_auto_20190210_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
