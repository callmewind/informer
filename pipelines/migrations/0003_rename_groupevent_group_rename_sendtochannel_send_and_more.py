# Generated by Django 4.0.4 on 2022-04-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_environment_slug_alter_environment_name'),
        ('pipelines', '0002_alter_pipeline_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupEvent',
            new_name='Group',
        ),
        migrations.RenameModel(
            old_name='SendToChannel',
            new_name='Send',
        ),
        migrations.AddField(
            model_name='pipelinestep',
            name='type',
            field=models.CharField(choices=[('delay', 'delay'), ('group', 'group'), ('send', 'send')], default='', max_length=50, verbose_name='type'),
            preserve_default=False,
        ),
    ]