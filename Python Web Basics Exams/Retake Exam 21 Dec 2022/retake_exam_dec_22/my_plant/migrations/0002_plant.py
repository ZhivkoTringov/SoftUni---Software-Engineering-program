# Generated by Django 4.2.2 on 2023-06-21 12:43

import django.core.validators
from django.db import migrations, models
import retake_exam_dec_22.my_plant.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_plant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), retake_exam_dec_22.my_plant.models.validate_letters_only])),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]