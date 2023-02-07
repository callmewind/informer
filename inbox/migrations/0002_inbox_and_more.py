# Generated by Django 4.1.4 on 2022-12-18 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flows", "0001_initial"),
        ("inbox", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inbox",
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
                ("title", models.CharField(max_length=100, verbose_name="title")),
                ("message", models.TextField(verbose_name="message")),
                ("url", models.URLField(blank=True, default="", verbose_name="url")),
                (
                    "image",
                    models.URLField(blank=True, default="", verbose_name="image"),
                ),
                (
                    "entry_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Additional data for custom implementations",
                        verbose_name="entry data",
                    ),
                ),
                (
                    "preview_context",
                    models.JSONField(
                        blank=True, default=dict, verbose_name="preview context"
                    ),
                ),
            ],
            options={
                "verbose_name": "send to inbox",
                "verbose_name_plural": "sending to inbox",
            },
            bases=("flows.flowstep",),
        ),
        migrations.RemoveIndex(
            model_name="inboxentry",
            name="inbox_inbox_site_id_edc2c0_idx",
        ),
        migrations.RemoveField(
            model_name="inboxentry",
            name="contact",
        ),
        migrations.AddField(
            model_name="inboxentry",
            name="contact_key",
            field=models.CharField(
                default=1, max_length=100, verbose_name="contact key"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inboxentry",
            name="image",
            field=models.URLField(blank=True, default="", verbose_name="image"),
        ),
        migrations.AddIndex(
            model_name="inboxentry",
            index=models.Index(
                fields=["site", "environment", "contact_key", "-date"],
                name="inbox_inbox_site_id_8648f7_idx",
            ),
        ),
    ]
