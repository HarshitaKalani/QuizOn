# Generated by Django 3.2.8 on 2022-03-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_questionfinal_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionfinal',
            name='label',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
