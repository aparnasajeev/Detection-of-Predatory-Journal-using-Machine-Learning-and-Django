# Generated by Django 3.0.3 on 2020-03-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0010_auto_20200308_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaltable',
            name='Email_of_Editor',
            field=models.CharField(choices=[('official', 'official'), ('gmail', 'gmail'), ('not available', 'not available')], max_length=200),
        ),
    ]
