# Generated by Django 2.2.20 on 2021-04-20 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prepaid_agreements', '0002_add_deleted_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prepaidagreement',
            options={'ordering': ['-effective_date', '-created_time']},
        ),
    ]
