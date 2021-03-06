# Generated by Django 2.1.5 on 2019-02-14 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0001_initial'),
        ('PE', '0011_auto_20190214_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='electeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electeur_allname', models.CharField(max_length=40)),
                ('candidat_cin', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='candidat_president',
            name='candidat_voter',
        ),
        migrations.AddField(
            model_name='electeur',
            name='candidat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PE.candidat_president'),
        ),
        migrations.AddField(
            model_name='electeur',
            name='electeur_departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumestc.Departement'),
        ),
    ]
