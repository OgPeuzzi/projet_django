# Generated by Django 4.1.7 on 2023-03-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=350)),
                ('Last_name', models.CharField(max_length=350)),
                ('Email', models.EmailField(max_length=200)),
                ('Message', models.TextField(max_length=350)),
            ],
        ),
    ]
