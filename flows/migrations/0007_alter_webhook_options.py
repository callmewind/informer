# Generated by Django 4.1.7 on 2023-03-27 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0006_donotdisturb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webhook',
            options={'verbose_name': 'webhook', 'verbose_name_plural': 'webhooks'},
        ),
    ]
