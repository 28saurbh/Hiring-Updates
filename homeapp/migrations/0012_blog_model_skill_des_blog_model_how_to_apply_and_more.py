# Generated by Django 4.0.2 on 2022-02-14 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0011_auto_20220213_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_model',
            name='Skill_des',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_model',
            name='how_to_apply',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_model',
            name='min_qulification',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
