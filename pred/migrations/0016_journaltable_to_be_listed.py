# Generated by Django 3.0.3 on 2020-03-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0015_auto_20200308_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='journaltable',
            name='to_be_listed',
            field=models.BooleanField(default=True),
        ),
    ]
