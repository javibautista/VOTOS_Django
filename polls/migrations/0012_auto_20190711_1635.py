# Generated by Django 2.2.1 on 2019-07-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20190711_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AddField(
            model_name='choice',
            name='op_correcta',
            field=models.BooleanField(default=False, verbose_name='Correct answer'),
        ),
    ]
