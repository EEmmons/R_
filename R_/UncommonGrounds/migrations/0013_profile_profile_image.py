# Generated by Django 2.0.2 on 2018-04-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0012_remove_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='', upload_to='profile_images'),
        ),
    ]