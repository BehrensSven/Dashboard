# Generated by Django 5.1 on 2024-11-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='category',
            field=models.CharField(choices=[('PERS', 'Persönlich'), ('ORG', 'Organisation'), ('EXM', 'Klausur')], default='PERS', max_length=4),
        ),
        migrations.AddField(
            model_name='appointment',
            name='type',
            field=models.CharField(choices=[('info', 'Info'), ('warnung', 'Warnung'), ('support', 'Support')], default='info', max_length=10),
        ),
        migrations.AddField(
            model_name='appointment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
