# Generated by Django 2.1.5 on 2019-02-23 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0010_utilisateur_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='utilisateur',
            new_name='User',
        ),
    ]
