# Generated by Django 3.2.8 on 2022-01-08 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_allquizes_questionfinal_quizfinal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionfinal',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='quizfinal',
            name='tutor',
        ),
        migrations.DeleteModel(
            name='AllQuizes',
        ),
        migrations.DeleteModel(
            name='QuestionFinal',
        ),
        migrations.DeleteModel(
            name='QuizFinal',
        ),
    ]