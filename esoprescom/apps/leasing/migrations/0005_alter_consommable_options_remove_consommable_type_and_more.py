# Generated by Django 5.0.1 on 2024-02-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0004_rename_model_consommable_modele_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consommable',
            options={'managed': True, 'ordering': ['-date', 'categorieproduit', 'typeproduit', 'reference'], 'verbose_name': 'Consommable', 'verbose_name_plural': 'Consommables'},
        ),
        migrations.RemoveField(
            model_name='consommable',
            name='type',
        ),
        migrations.AddField(
            model_name='consommable',
            name='categorieproduit',
            field=models.CharField(choices=[('HP', 'Produit HP'), ('Produit LexMask', 'Produit LexMask'), ('Produit Canon', 'Produit Canon'), ('Autres', 'Autres')], default='Produit LexMask', max_length=30, verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='consommable',
            name='typeproduit',
            field=models.CharField(choices=[('Cartouche', 'Cartouche'), ('Photoconducteur', 'Photoconducteur'), ('Kits', 'Kits '), ('fuser LexMark', 'Fuser LexMark'), ('Papier RAM', 'Papier RAM')], default='Papier RAM', max_length=20, verbose_name='Produit'),
        ),
    ]
