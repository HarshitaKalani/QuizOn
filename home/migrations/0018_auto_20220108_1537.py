# Generated by Django 3.2.8 on 2022-01-08 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0017_auto_20220108_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allquizes',
            name='connect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userFinal', to='home.usercontainer'),
        ),
        migrations.AlterField(
            model_name='allquizes',
            name='tutorName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
