# Generated by Django 3.1.2 on 2020-10-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0002_auto_20201028_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='audio',
            field=models.CharField(blank=True, default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='picture',
            field=models.CharField(blank=True, default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='ru1',
            field=models.CharField(blank=True, default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='ru2',
            field=models.CharField(blank=True, default='', max_length=128),
            preserve_default=False,
        ),
    ]