# Generated by Django 2.2 on 2019-05-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0045_auto_20190531_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laurea',
            name='image',
            field=models.ImageField(upload_to='Laurea/images'),
        ),
    ]
