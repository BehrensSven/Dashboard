# Generated by Django 5.1 on 2024-11-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_studentmodule_completion_date_studentmodule_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstudyprogram',
            name='enrollment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userstudyprogram',
            name='time_model',
            field=models.IntegerField(blank=True, choices=[(3, '3 Jahre'), (4, '4 Jahre'), (6, '6 Jahre')], null=True),
        ),
    ]
