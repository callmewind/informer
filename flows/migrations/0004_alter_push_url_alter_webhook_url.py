# Generated by Django 4.1.4 on 2023-01-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flows", "0003_alter_flow_preview_context"),
    ]

    operations = [
        migrations.AlterField(
            model_name="push",
            name="url",
            field=models.CharField(max_length=500, verbose_name="url"),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="url",
            field=models.CharField(max_length=500, verbose_name="url"),
        ),
    ]
