# Generated by Django 3.2.8 on 2022-01-11 10:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionfinal',
            name='que',
            field=ckeditor.fields.RichTextField(default=' '),
        ),
    ]
