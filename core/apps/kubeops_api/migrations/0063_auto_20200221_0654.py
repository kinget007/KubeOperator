# Generated by Django 2.2.10 on 2020-02-21 06:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kubeops_api', '0062_auto_20200221_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clusterhealthhistory',
            name='date_type',
            field=models.CharField(choices=[('HOUR', 'HOUR'), ('DAY', 'DAY')], default='HOUR', max_length=255),
        ),
    ]
