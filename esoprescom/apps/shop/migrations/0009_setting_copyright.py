# Generated by Django 5.0.6 on 2024-05-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='copyright',
            field=models.CharField(default='Copyright', max_length=255),
            preserve_default=False,
        ),
    ]
