# Generated by Django 4.1.4 on 2023-01-07 13:19

from django.db import migrations, models
import flows.models.flow


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0002_remove_email_preview_context_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='preview_context',
            field=models.JSONField(blank=True, default=flows.models.flow.default_preview_context, help_text='Data defined here will be used for generating previews in steps using context data.', verbose_name='preview context'),
        ),
    ]