# Generated by Django 3.0.5 on 2020-04-23 06:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('sqrt', models.IntegerField()),
                ('plot_size', models.IntegerField()),
                ('price', models.CharField(max_length=100)),
                ('bedroom', models.IntegerField()),
                ('listing_date', models.DateTimeField(default=datetime.datetime.now)),
                ('main_photo', models.ImageField(upload_to='image')),
                ('optional_photo1', models.ImageField(upload_to='image')),
                ('optional_photo2', models.ImageField(upload_to='image')),
                ('optional_photo3', models.ImageField(upload_to='image')),
                ('optional_photo4', models.ImageField(upload_to='image')),
                ('optional_photo5', models.ImageField(upload_to='image')),
                ('optional_photo6', models.ImageField(upload_to='image')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtor')),
            ],
        ),
    ]
