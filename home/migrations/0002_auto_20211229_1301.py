# Generated by Django 3.2.9 on 2021-12-29 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='query',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
