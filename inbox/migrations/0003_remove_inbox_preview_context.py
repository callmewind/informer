# Generated by Django 4.1.4 on 2023-01-07 13:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inbox", "0002_inbox_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inbox",
            name="preview_context",
        ),
    ]
