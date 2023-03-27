# Generated by Django 4.1.7 on 2023-03-27 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('accounts', '0002_alter_environment_private_key_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='environment',
            unique_together={('site', 'name'), ('site', 'slug')},
        ),
    ]
