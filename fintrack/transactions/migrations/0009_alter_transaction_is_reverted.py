# Generated by Django 4.2.13 on 2024-07-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_transaction_is_reverted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='is_reverted',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]