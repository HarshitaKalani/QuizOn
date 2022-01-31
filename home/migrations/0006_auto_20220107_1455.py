# Generated by Django 3.2.9 on 2022-01-07 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211230_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['sno']},
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='dateStamp',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to='home.quiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='sno',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='email',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('quiz', 'sno')},
        ),
        migrations.RemoveField(
            model_name='question',
            name='email',
        ),
    ]