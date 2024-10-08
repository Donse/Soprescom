# Generated by Django 5.0.6 on 2024-05-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_category_is_mega'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=25)),
                ('button_link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='navcollection/%Y/%m/%d/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
