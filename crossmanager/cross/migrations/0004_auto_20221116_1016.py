# Generated by Django 2.2.19 on 2022-11-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0003_auto_20221109_1448'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='cross',
            constraint=models.CheckConstraint(check=models.Q(('ten__gte', 0), ('fifteen__gte', 0), ('twenty__gte', 0), ('twentyfive__gte', 0), ('thirty__gte', 0), ('thirtyfive__gte', 0), _connector='OR'), name='fields not minus'),
        ),
    ]
