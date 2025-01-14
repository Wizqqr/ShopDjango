# Generated by Django 5.0.7 on 2024-07-19 09:57

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewWorkerUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.PositiveIntegerField(default=18, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(99)])),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('developer_type', models.CharField(choices=[('backend', 'Backend'), ('frontend', 'Frontend'), ('mobile', 'Mobile')], max_length=100)),
                ('years_of_experience', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('salary', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3000)])),
                ('level', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
