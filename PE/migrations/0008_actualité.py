# Generated by Django 2.1.5 on 2019-02-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0007_auto_20190210_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='actualité',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=40)),
                ('image', models.ImageField(default='default.png', upload_to='')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
