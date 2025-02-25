# Generated by Django 5.1 on 2024-11-22 07:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_mymodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('scheduled_at', models.DateTimeField()),
                ('users', models.ManyToManyField(related_name='appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
