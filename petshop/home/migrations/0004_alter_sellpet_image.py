# Generated by Django 4.1.7 on 2023-10-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_sellpet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellpet',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]