# Generated by Django 4.2.5 on 2023-09-29 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student',
            new_name='login',
        ),
        migrations.RenameModel(
            old_name='student2',
            new_name='signup',
        ),
    ]