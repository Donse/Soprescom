# Generated by Django 5.0.6 on 2024-05-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_setting_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='email',
            field=models.EmailField(default='info@soprescom.net', max_length=10),
        ),
    ]
