# Generated by Django 3.1.7 on 2021-07-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210719_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='views',
            options={},
        ),
        migrations.AlterField(
            model_name='views',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Id поста'),
        ),
    ]
