# Generated by Django 5.0.7 on 2024-07-19 09:52

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Upload a picture please')),
                ('second_model', models.ImageField(null=True, upload_to='images/', verbose_name='Upload a second model')),
                ('third_model', models.ImageField(null=True, upload_to='images/', verbose_name='Upload a third model')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Write some information')),
                ('in_stock', models.BooleanField(default=True, null=True, verbose_name='In Stock')),
                ('price_for_first', models.PositiveIntegerField(default=1000, null=True)),
                ('price_for_second', models.PositiveIntegerField(default=1000, null=True)),
                ('price_for_third', models.PositiveIntegerField(default=1000, null=True)),
                ('sale', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Is has a sale?')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_phone', to='telephone.phone')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]