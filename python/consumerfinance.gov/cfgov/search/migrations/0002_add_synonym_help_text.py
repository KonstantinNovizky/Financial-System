# Generated by Django 2.2.23 on 2021-06-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synonym',
            name='synonym',
            field=models.CharField(help_text='A comma-separated list of words that are synonyms', max_length=500),
        ),
    ]