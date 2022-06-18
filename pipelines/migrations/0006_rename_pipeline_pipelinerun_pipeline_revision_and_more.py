# Generated by Django 4.0.5 on 2022-06-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0005_email_from_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pipelinerun',
            old_name='pipeline',
            new_name='pipeline_revision',
        ),
        migrations.AddField(
            model_name='pipelinerun',
            name='pipeline_id',
            field=models.UUIDField(default=1, editable=False, verbose_name='id'),
            preserve_default=False,
        ),
    ]