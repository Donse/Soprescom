# Generated by Django 5.0.6 on 2024-06-06 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapresvente', '0009_rename_idassemblage_assemblagereparation_idassemblage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandesav',
            name='statut',
            field=models.CharField(choices=[('commande placée', 'commande placée'), ('pending', 'pending')], default='pending', max_length=30, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='suivicommandesav',
            name='statut',
            field=models.CharField(choices=[('logistique', 'logistique'), ('Réception dépôt France ', 'Réception dépôt France'), ('Reception dépôt Dubaï ', 'Réception dépôt Dubaï'), ('Sous Douane Malienne', 'Sous Douane Malienne'), ('Reçu', 'Reçu')], default='logistique', max_length=30, verbose_name='Statut'),
        ),
    ]
