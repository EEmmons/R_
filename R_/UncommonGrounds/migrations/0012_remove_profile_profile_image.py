# Generated by Django 2.0.2 on 2018-04-08 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0011_auto_20180408_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
    ]
