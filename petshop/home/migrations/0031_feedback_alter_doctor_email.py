# Generated by Django 4.1.7 on 2023-10-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_remove_doctor_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
