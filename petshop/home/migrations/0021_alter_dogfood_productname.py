# Generated by Django 4.1.7 on 2023-10-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_dogfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogfood',
            name='productName',
            field=models.CharField(max_length=300),
        ),
    ]
