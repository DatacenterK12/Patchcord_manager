# Generated by Django 2.2.19 on 2022-11-18 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0006_auto_20221118_1200'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='mmr',
            name='fields not minus',
        ),
        migrations.AddField(
            model_name='mmr',
            name='five',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddConstraint(
            model_name='mmr',
            constraint=models.CheckConstraint(check=models.Q(('one__gte', 0), ('two__gte', 0), ('three__gte', 0), ('five__gte', 0)), name='fields not minus'),
        ),
    ]