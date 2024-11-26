# Generated by Django 5.0.2 on 2024-11-26 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=100)),
                ('voice_id', models.CharField(max_length=100, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('campaign_type', models.CharField(choices=[('Inbound', 'Inbound'), ('Outbound', 'Outbound')], max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Paused', 'Paused'), ('Completed', 'Completed')], default='Running', max_length=50)),
                ('agents', models.ManyToManyField(related_name='campaigns', to='campaigns.agent')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('cost', models.FloatField()),
                ('outcome', models.CharField(max_length=100)),
                ('call_duration', models.FloatField()),
                ('recording', models.URLField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('transcription', models.TextField(blank=True, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='campaigns.campaign')),
            ],
        ),
    ]
