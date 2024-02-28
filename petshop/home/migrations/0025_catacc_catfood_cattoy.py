# Generated by Django 4.1.7 on 2023-10-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_dogacc_dogtoy'),
    ]

    operations = [
        migrations.CreateModel(
            name='catAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=300)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='catFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=300)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='catToy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=300)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
