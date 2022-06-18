# Generated by Django 4.0.4 on 2022-06-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_alter_channel_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailchannel',
            name='security',
            field=models.CharField(choices=[('none', 'none'), ('ssl', 'TSL/SSL'), ('starttls', 'STARTTLS')], default='ssl', max_length=20, verbose_name='security'),
        ),
    ]