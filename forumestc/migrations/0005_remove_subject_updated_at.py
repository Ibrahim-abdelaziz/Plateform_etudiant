# Generated by Django 2.1.5 on 2019-02-17 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0004_utilisateur_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='updated_at',
        ),
    ]
