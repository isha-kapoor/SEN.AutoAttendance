# Generated by Django 3.0.4 on 2020-03-29 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('prof_section', '0003_attendancerecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('courses', models.CharField(max_length=100)),
            ],
        ),
    ]
