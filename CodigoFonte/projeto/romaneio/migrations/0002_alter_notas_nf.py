# Generated by Django 4.1.7 on 2023-03-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romaneio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='nf',
            field=models.IntegerField(verbose_name='NF'),
        ),
    ]