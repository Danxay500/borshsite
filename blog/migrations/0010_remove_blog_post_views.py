# Generated by Django 3.1.7 on 2021-07-19 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210719_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='post_views',
        ),
    ]
