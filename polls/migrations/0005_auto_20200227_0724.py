# Generated by Django 3.0.3 on 2020-02-26 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200227_0608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': '答案', 'verbose_name_plural': '答案'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'question', 'verbose_name_plural': 'question'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question', verbose_name='调研问题'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_txt',
            field=models.CharField(max_length=200, verbose_name='question'),
        ),
    ]
