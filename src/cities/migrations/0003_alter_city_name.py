# Generated by Django 4.0.5 on 2022-06-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='shahar'),
        ),
    ]