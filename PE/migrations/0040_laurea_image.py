# Generated by Django 2.2 on 2019-05-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0039_remove_laurea_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='laurea',
            name='image',
            field=models.ImageField(default='im.jpg', upload_to='arts/'),
        ),
    ]
