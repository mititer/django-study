# Generated by Django 3.0.3 on 2020-02-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200227_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='active',
            field=models.IntegerField(verbose_name='active'),
        ),
    ]