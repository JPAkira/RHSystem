# Generated by Django 3.2.4 on 2021-06-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='cargo',
            field=models.CharField(max_length=40),
        ),
    ]