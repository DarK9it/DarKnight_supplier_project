# Generated by Django 4.2.2 on 2023-06-30 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0017_alter_paiement_statut'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paiement',
            old_name='statut',
            new_name='status',
        ),
    ]
