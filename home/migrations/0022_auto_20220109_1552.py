# Generated by Django 3.2.8 on 2022-01-09 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0021_auto_20220109_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllQuizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='QuizFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfQuiz', models.CharField(max_length=100)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizesFinal', to='home.allquizes')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('ans', models.CharField(max_length=100)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionFinal', to='home.quizfinal')),
            ],
        ),
        migrations.AddField(
            model_name='allquizes',
            name='connect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userFinal', to='home.usercontainer'),
        ),
        migrations.AddField(
            model_name='allquizes',
            name='tutorName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
