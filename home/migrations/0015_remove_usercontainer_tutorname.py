# Generated by Django 3.2.8 on 2022-01-08 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220108_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontainer',
            name='tutorName',
        ),
    ]
