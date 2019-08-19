# Generated by Django 2.2.1 on 2019-07-11 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190710_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=100, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='op_correcta',
            field=models.BooleanField(default=False, verbose_name='Correct answer'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Question'),
        ),
    ]
