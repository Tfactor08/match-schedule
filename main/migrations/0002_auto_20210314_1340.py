# Generated by Django 3.0.7 on 2021-03-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]
