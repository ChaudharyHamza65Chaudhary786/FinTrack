# Generated by Django 4.2.13 on 2024-07-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='acc_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='holder_name',
            new_name='title',
        ),
    ]
