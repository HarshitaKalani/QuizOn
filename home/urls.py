from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('',views.index, name='home'),
    path("login",views.loginPage, name='loginPage'),
    path("loginuser",views.loginuser, name='loginuser'),
    path("logout",views.logoutuser, name='logoutuser'),
    path("signup",views.signUp, name='signUp'),
    path("handleSignUpTeacher",views.handleSignUpTeacher, name='handleSignUpTeacher'),
    path("handleSignUpStudent",views.handleSignUpStudent, name='handleSignUpStudent'),
    path("CreateQuiz",views.CreateQuiz, name='CreateQuiz'),
    path("contact" ,views.contact, name='contact'),
    path("quizQuery" ,views.quizQuery, name='quizQuery'),
    path("handleMultipleChoice" ,views.handleMultipleChoice, name='handleMultipleChoice'),
    path("handleQuestionCreation" ,views.handleQuestionCreation, name='handleQuestionCreation'),
    path("temp" ,views.temp, name='temp'),
    path("subjective" ,views.subjective, name='subjective'),
    path("handleSubjective" ,views.handleSubjective, name='handleSubjective'),
    path("handlePoll" ,views.handlePoll, name='handlePoll'),
    path("handlePollCreator" ,views.handlePollCreator, name='handlePollCreator'),
    path("handleImport" ,views.handleImport, name='handleImport'),
    path("handleImportSpreadsheet" ,views.handleImportSpreadsheet, name='handleImportSpreadsheet'),
    path("handleStartQuiz" ,views.handleStartQuiz, name='handleStartQuiz'),
    path("handleEndQuiz" ,views.handleEndQuiz, name='handleEndQuiz'),
    path("handleQuizStarted" ,views.handleQuizStarted, name='handleQuizStarted'),
    path("handleNextQuestion" ,views.handleNextQuestion, name='handleNextQuestion'),
    path("handleDeleteQuiz" ,views.handleDeleteQuiz, name='handleDeleteQuiz'),
    path("handleAnswerResponse" ,views.handleAnswerResponse, name='handleAnswerResponse'),
    path("handleSave" ,views.handleSave, name='handleSave'),
<<<<<<< Updated upstream
    path("newHandleAnswerResponse" ,views.newHandleAnswerResponse, name='newHandleAnswerResponse'),

=======
>>>>>>> Stashed changes





















]