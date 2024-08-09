# Generated by Django 5.0.4 on 2024-08-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_factory_time_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='market_launch_date',
            field=models.DateTimeField(verbose_name='Дата выхода продукта на рынок'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='time_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='market_launch_date',
            field=models.DateTimeField(verbose_name='Дата выхода продукта на рынок'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='time_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='market_launch_date',
            field=models.DateTimeField(verbose_name='Дата выхода продукта на рынок'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='time_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
    ]
