# Generated by Django 4.1.7 on 2023-02-25 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='modele',
            name='modele',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='producteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=100)),
                ('representant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicule.representant', verbose_name='nom')),
            ],
        ),
    ]
