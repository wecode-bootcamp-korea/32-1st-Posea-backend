# Generated by Django 4.0.4 on 2022-05-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
