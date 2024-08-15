# Generated by Django 5.0.6 on 2024-06-24 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapresvente', '0023_alter_recouvrement_droit_douane_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloturedossier',
            old_name='date_cloture',
            new_name='resp_dossier',
        ),
        migrations.RemoveField(
            model_name='cloturedossier',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='cloturedossier',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='cloturedossier',
            name='recouvrement_ID',
        ),
        migrations.RemoveField(
            model_name='cloturedossier',
            name='recouvrement_Type',
        ),
        migrations.RemoveField(
            model_name='cloturedossier',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='cloturedossier',
            name='recouvrement',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recouvrements', to='serviceapresvente.recouvrement'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cloturedossier',
            name='Numero_Dossier',
            field=models.CharField(max_length=30, verbose_name='Numero_Dossier'),
        ),
        migrations.AlterField(
            model_name='cloturedossier',
            name='statut',
            field=models.CharField(max_length=30, verbose_name='Clôture Dossier'),
        ),
        migrations.AlterField(
            model_name='recouvrement',
            name='statutDevea',
            field=models.CharField(choices=[('facturation HP, a completer', 'facturation HP, a completer'), ('Dossier HP complet', 'Dossier HP complet'), ('Dossier HP payé', 'Dossier HP payé'), ('Dossier HP non payé', 'Dossier HP non payé')], default='facturation HP, a completer', max_length=40, verbose_name='Statut'),
        ),
        migrations.DeleteModel(
            name='RecouvrementDevea',
        ),
    ]
