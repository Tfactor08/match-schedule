# Generated by Django 3.0.7 on 2021-03-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210314_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.TimeField(),
        ),
    ]