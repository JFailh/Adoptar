# Generated by Django 4.1.7 on 2023-06-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('raza', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
