# Generated by Django 2.2.16 on 2023-01-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0008_auto_20221228_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('lenght', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, db_index=True, verbose_name='дата')),
            ],
        ),
    ]
