# Generated by Django 2.2.24 on 2022-04-15 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='key',
            old_name='first_name',
            new_name='key',
        ),
    ]
