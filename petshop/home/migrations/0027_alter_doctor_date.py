# Generated by Django 4.1.7 on 2023-10-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='date',
            field=models.DateField(),
        ),
    ]
