# Generated by Django 2.2 on 2019-05-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0044_auto_20190531_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laurea',
            name='image',
            field=models.ImageField(default='imm.png', upload_to=''),
        ),
    ]
