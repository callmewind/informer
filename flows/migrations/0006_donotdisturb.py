# Generated by Django 4.1.6 on 2023-03-06 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("flows", "0005_webhook_skip_ssl"),
    ]

    operations = [
        migrations.CreateModel(
            name="DoNotDisturb",
            fields=[
                (
                    "flowstep_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="flows.flowstep",
                    ),
                ),
                ("start", models.TimeField(verbose_name="start")),
                ("end", models.TimeField(verbose_name="end")),
            ],
            options={
                "verbose_name": "do not disturb",
                "verbose_name_plural": "do not disturb",
            },
            bases=("flows.flowstep",),
        ),
    ]
