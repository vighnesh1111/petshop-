# Generated by Django 4.1.7 on 2023-10-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_selldog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selldog',
            name='image',
        ),
        migrations.AddField(
            model_name='selldog',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
