# Generated by Django 5.0.6 on 2024-06-04 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapresvente', '0007_remove_sav_request_validation_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sav_request',
            old_name='facture_fornisseur',
            new_name='facture_fournisseur',
        ),
    ]
