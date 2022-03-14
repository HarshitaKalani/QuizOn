from tkinter import Image
from django.forms import ModelForm
from .models import *
from django import forms
# import ckeditor
# from djrichtextfield.widgets import RichTextWidget

class StudentForm(ModelForm):
    # question=forms.CharField(widget=RichTextWidget())
    class Meta:
        model=QuestionFinal
        fields=('que',)
class ImageForm(ModelForm):
    class Meta:
        model=QuestionFinal
        fields=('queImage',)
        
