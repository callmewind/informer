# Generated by Django 4.1.3 on 2022-11-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='private_key',
            field=models.CharField(max_length=40, verbose_name='private key'),
        ),
        migrations.AlterField(
            model_name='environment',
            name='public_key',
            field=models.CharField(max_length=40, verbose_name='public key'),
        ),
    ]