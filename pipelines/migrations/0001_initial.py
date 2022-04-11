# Generated by Django 4.0.3 on 2022-04-11 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('trigger', models.CharField(db_index=True, max_length=150, verbose_name='trigger')),
                ('environments', models.ManyToManyField(related_name='pipelines', to='configuration.environment')),
            ],
            options={
                'verbose_name': 'pipeline',
                'verbose_name_plural': 'pipelines',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PipelineStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(verbose_name='order')),
                ('pipeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pipelines.pipeline', verbose_name='pipeline')),
            ],
            options={
                'verbose_name': 'pipeline step',
                'verbose_name_plural': 'pipeline steps',
                'ordering': ('pipeline', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Delay',
            fields=[
                ('pipelinestep_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pipelines.pipelinestep')),
                ('time', models.DurationField(verbose_name='time')),
            ],
            bases=('pipelines.pipelinestep',),
        ),
        migrations.CreateModel(
            name='GroupEvent',
            fields=[
                ('pipelinestep_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pipelines.pipelinestep')),
                ('window', models.DurationField(verbose_name='time window')),
                ('key', models.CharField(max_length=150, verbose_name='grouping key')),
            ],
            bases=('pipelines.pipelinestep',),
        ),
        migrations.CreateModel(
            name='SendToChannel',
            fields=[
                ('pipelinestep_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pipelines.pipelinestep')),
                ('only_unread', models.BooleanField(default=True, verbose_name='unread only')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuration.channel')),
            ],
            bases=('pipelines.pipelinestep',),
        ),
    ]
