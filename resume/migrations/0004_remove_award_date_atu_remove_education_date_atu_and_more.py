# Generated by Django 4.1.7 on 2023-02-21 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_award_date_atu_alter_education_date_atu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='date_atu',
        ),
        migrations.RemoveField(
            model_name='education',
            name='date_atu',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='date_atu',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='date_atu',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_atu',
        ),
    ]