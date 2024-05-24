# Generated by Django 5.0.6 on 2024-05-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('decrypt', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
