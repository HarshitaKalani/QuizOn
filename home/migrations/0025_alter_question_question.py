# Generated by Django 3.2.8 on 2022-01-11 09:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_student_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor.fields.RichTextField(default=' '),
        ),
    ]
