# Generated by Django 4.1.7 on 2023-02-21 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_user_email_alter_award_date_atu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='date_atu',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 21, 0, 54, 25, 745940)),
        ),
        migrations.AlterField(
            model_name='education',
            name='date_atu',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 21, 0, 54, 25, 743673)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_atu',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 21, 0, 54, 25, 742385)),
        ),
        migrations.AlterField(
            model_name='skill',
            name='date_atu',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 21, 0, 54, 25, 744813)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_atu',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 21, 0, 54, 25, 741126)),
        ),
    ]