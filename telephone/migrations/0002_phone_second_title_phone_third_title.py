# Generated by Django 5.0.7 on 2024-07-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telephone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='second_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='third_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]