# Generated by Django 4.1.3 on 2022-11-30 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0004_alter_contact_key"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="public_key",
        ),
        migrations.AddField(
            model_name="contact",
            name="auth_key",
            field=models.CharField(
                default=1, max_length=40, verbose_name="auth key"),
            preserve_default=False,
        ),
    ]
