# Generated by Django 2.2.4 on 2020-08-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0003_auto_20200820_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='description',
            field=models.TextField(default=''),
        ),
    ]