# Generated by Django 4.1.7 on 2023-02-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=200)),
                ('classe', models.CharField(max_length=50)),
                ('cycle', models.CharField(max_length=50)),
                ('nom_pere', models.CharField(max_length=40)),
                ('nom_mere', models.CharField(max_length=40)),
                ('naissance', models.DateField()),
            ],
        ),
    ]