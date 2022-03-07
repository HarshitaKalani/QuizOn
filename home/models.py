from django.db import models
from django.db.models.fields import IntegerField
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField
from django_mysql.models import ListCharField
from rest_framework import serializers
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    remark=RichTextField(default=" ")

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    
    query=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
class Quiz(models.Model):
    email=models.CharField(max_length=122, default=None)
    name=models.CharField(max_length=122, default=None)
    # dateStamp=models.DateField()
    # question=models.JSONField(models.ForeignKey(Question, on_delete=models.CASCADE))

class Question(models.Model):
    quiz=models.ForeignKey(Quiz, related_name='quizes', on_delete=models.CASCADE, default=None)
    sno=models.IntegerField(default=None)
    question = RichTextField(default=" ")
    op1 = models.CharField(max_length=200,default=None)
    op2 = models.CharField(max_length=200,default=None)
    op3 = models.CharField(max_length=200,default=None)
    op4 = models.CharField(max_length=200,default=None)
    ans = models.CharField(max_length=200,default=None)
    class Meta:
        unique_together=['quiz', 'sno']
        ordering =['sno']
    def __str__(self):
        return '%d:%s' %(self.sno, self.question)
    
    # class QuizSerializer(serializers.ModelSerializer):

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)

class QuestionTrack(models.Model):
    album = models.ForeignKey(Album, related_name='quizes', on_delete=models.CASCADE)
    number = models.IntegerField()
    quest = models.CharField(max_length=100)
    ans = models.IntegerField()

    class Meta:
        unique_together = ['album', 'number']
        ordering = ['number']

    def __str__(self):
        return '%d: %s' % (self.number, self.quest)

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class QuestionTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTrack
        fields = ['number', 'quest', 'ans']

class AlbumSerializer(serializers.ModelSerializer):
    quizes = QuestionTrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'quizes']

class UserContainer(models.Model):
    pass

class AllQuizes(models.Model):
    tutorName=models.ForeignKey(User, on_delete=models.CASCADE)
    connect=models.ForeignKey(UserContainer,related_name="userFinal",on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.tutorName)

class QuizFinal(models.Model):
    timeStamp=models.DateField(default=None)
    tutor=models.ForeignKey(AllQuizes, related_name='quizesFinal', on_delete=models.CASCADE)
    nameOfQuiz=models.CharField(max_length=100)
    bool=models.BooleanField(default=None)
    code=models.UUIDField(default=uuid.uuid4)
    quizTimer=models.IntegerField(default=10)
    def __str__(self):
        return '%s' %(self.nameOfQuiz)

class QuestionFinal(models.Model):
    tutor=models.ForeignKey(QuizFinal, related_name='questionFinal', on_delete=models.CASCADE)
    # que=models.CharField(max_length=100)
    # que=models.CharField(max_length=100)
    # que=models.CharField(max_length=100)
    label=models.CharField(max_length=100,default=None)
    questionTimer=models.IntegerField(default=10)
    marks=models.IntegerField(default=10)
    que=RichTextField(default=" ")
    number = models.IntegerField()
    op1=RichTextField(default=" ")
    op2=RichTextField(default=" ")
    op3=RichTextField(default=" ")
    op4=RichTextField(default=" ")
    ans=models.CharField(max_length=100)

class StudentFinal(models.Model):
    quiz=models.ForeignKey(QuizFinal,on_delete=models.CASCADE)
    nameOfStudent=models.CharField(max_length=100,default=" ")
    def __str__(self):
        return '%s' %(self.nameOfStudent)

class AnswerFinal(models.Model):
    quiz=models.ForeignKey(QuizFinal,on_delete=models.CASCADE)
    question=models.ForeignKey(QuestionFinal,on_delete=models.CASCADE)
    student=models.ForeignKey(StudentFinal,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100,default=" ")
    def __str__(self):
        return '%s' %(self.student)
        
class QuestionFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionFinal
        fields=['tutor','que','number','ans']

class QuizFinalSerializer(serializers.ModelSerializer):
    questionFinal=QuestionFinalSerializer(many=True, read_only=True)

    class Meta:
        model= QuizFinal
        fields=['tutor','nameOfQuiz','questionFinal']

class AllQuizesSerializer(serializers.ModelSerializer):
    quizesFinal=QuizFinalSerializer(many=True, read_only=True)

    class Meta:
        model = AllQuizes
        fields=['tutorName','quizesFinal']

class UserContainerSerializer(serializers.ModelSerializer):
    userFinal=AllQuizesSerializer(many=True, read_only=True)

    class Meta:
        model = UserContainer
        fields= ['userFinal']


        
# class AllQuizes(models.Model):
#     email=models.CharField(max_length=122)
#     Listofquizes=ArrayField(base_field=models.ForeignKey(Quiz, on_delete=models.CASCADE))
    



# class createuserform(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['username', 'password']
# class addQuestionform(ModelForm):
#     class Meta:
#         model=Question
#         fields="__all__"
