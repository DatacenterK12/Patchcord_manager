# Generated by Django 2.2.16 on 2023-01-10 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0010_auto_20230110_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cross',
            options={'verbose_name': 'Патчорд', 'verbose_name_plural': 'Патчорды'},
        ),
        migrations.AlterModelOptions(
            name='mmr',
            options={'verbose_name': 'Патчорд MMR', 'verbose_name_plural': 'Патчорды MMR'},
        ),
        migrations.AlterModelOptions(
            name='new_stat',
            options={'ordering': ['-date'], 'verbose_name': 'Вычитание', 'verbose_name_plural': 'Вычитания'},
        ),
        migrations.AlterModelOptions(
            name='statistic',
            options={'verbose_name': 'Статистика', 'verbose_name_plural': 'Статистика'},
        ),
    ]
