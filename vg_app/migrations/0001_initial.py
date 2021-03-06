# Generated by Django 4.0.3 on 2022-04-07 17:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artist_ID', models.IntegerField(default=0, unique=True)),
                ('Name', models.CharField(max_length=50)),
                ('Artist_url', models.CharField(max_length=100)),
                ('Birth_date', models.DateField()),
                ('Birth_place', models.CharField(max_length=500)),
                ('Death_date', models.DateField()),
                ('Death_place', models.CharField(max_length=500)),
                ('Image', models.CharField(blank=True, max_length=500, null=True)),
                ('Wikipedia', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color', models.CharField(max_length=6)),
                ('Quantity', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture_ID', models.IntegerField(default=0, unique=True)),
                ('Title', models.CharField(max_length=50)),
                ('Year', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2022)])),
                ('Width', models.PositiveSmallIntegerField()),
                ('Height', models.PositiveSmallIntegerField()),
                ('Location', models.CharField(max_length=50, null=True)),
                ('Genre', models.CharField(blank=True, max_length=50, null=True)),
                ('Style', models.CharField(blank=True, max_length=50, null=True)),
                ('Size_x', models.FloatField(blank=True, null=True)),
                ('Size_y', models.FloatField(blank=True, null=True)),
                ('Gallery_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Tags', models.CharField(max_length=200, null=True)),
                ('Artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vg_app.artist')),
                ('Color', models.ManyToManyField(to='vg_app.color')),
            ],
            options={
                'ordering': ['Artist__Name', django.db.models.expressions.OrderBy(django.db.models.expressions.F('Year'), nulls_last=True), 'Title'],
            },
        ),
    ]
