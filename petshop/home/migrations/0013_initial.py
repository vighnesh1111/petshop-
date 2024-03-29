# Generated by Django 4.1.7 on 2023-10-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0012_delete_hotel_delete_sellpet'),
    ]

    operations = [
        migrations.CreateModel(
            name='sellDog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('breed', models.CharField(choices=[('german shephard', 'german shephard'), ('pug', 'pug'), ('pitbull', 'pitbull'), ('lab', 'lab'), ('bulldog', 'bulldog')], max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('phone', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
