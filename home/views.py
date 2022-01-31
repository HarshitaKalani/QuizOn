from django.shortcuts import render, HttpResponse, redirect
from django.http import response, HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
from .forms import StudentForm
from home.models import Contact
from django.contrib import messages
from .models import *
import pandas as pd
from .resources import QuestionFinalResource
from django.contrib import messages
from tablib import Dataset
from datetime import *

# Create your views here.
def index(request):
    return render (request, "index.html")
def loginPage(request):
    return render (request, "login.html")
def temp(request):
    form= StudentForm
    mydict={
        'form' :form
    }
    return render (request, 'temp.html',context=mydict)

@csrf_exempt
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if(user.is_superuser):
                first=AllQuizes.objects.filter(tutorName=user)
                quizes=[]
                for i in first.iterator():
                    quiz1=QuizFinal.objects.filter(tutor=i)
                    quizes.append(quiz1)
                quizes.reverse()
                return render(request,"indexLogged.html",{"username":username,"CreateQuiz":"CreateQuiz","ContentDescription":"Teacher Here!","YourQuizes":"Your Quizes","quizes":(quizes),"len":len(quizes)})
            else:
                return render(request,"indexLogged.html",{"username":username,"CreateQuiz":"JoinQuiz","ContentDescription":"Student Here!","YourQuizes":"Join Quiz"})

        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")

def signUp(request):
    return render(request, "studentTeacher.html")

def handleSignUpTeacher(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['confirmPassword']

        if(pass1==pass2):
            myuser=User.objects.create_user(username=username,email=email,password=pass1)
            myuser.is_superuser=True
            myuser.is_staff=True

            myuser.save()
            return render(request,"indexLogged.html",{"username":username,"CreateQuiz":"CreateQuiz","ContentDescription":"Teacher Here!"})
        else:
            return redirect("studentTeacher.html")
def handleSignUpStudent(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['confirmPassword']

        if(pass1==pass2):
            myuser=User.objects.create_user(username=username,email=email,password=pass1)
            myuser.is_superuser=False
            myuser.save()
            return render(request,"indexLogged.html",{"username":username,"CreateQuiz":"JoinQuiz","ContentDescription":"Student Here!"})
        else:
            return redirect("studentTeacher.html")

def contact(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
       
        query=request.POST.get('query')
        date=request.POST.get('date')
        contact=Contact(name=username, email=email, query=query, date=date)
        contact.save()
        messages.success(request, 'Your message has been sent')
        

    return render(request, 'contact.html')

def CreateQuiz(request):
    current_user=request.user
    if(current_user.is_superuser):
        return render(request,"createQuiz.html",{"createQuiz":"Create Quiz","NameOfTheQuiz": "Name the Quiz", "create": "create"})
    else:
        return render(request,"createQuiz.html",{"createQuiz":"Join Quiz","NameOfTheQuiz": "Code of the Quiz", "create": "Join"})
def contact(request):
    return render (request, "contact.html")
def is_valid_uuid(value):
    try:
        uuid.UUID(value)
 
        return True
    except ValueError:
        return False

def quizQuery(request):
    if request.method=="POST":
        nameQuiz=request.POST.get('nameQuiz')
        current_user=request.user

        
        if(current_user.is_superuser):
            universalContainer=UserContainer.objects.filter()[0]
            first=AllQuizes.objects.create(tutorName=current_user,connect=universalContainer)
            quiz1=QuizFinal.objects.create(tutor=first,nameOfQuiz=nameQuiz,timeStamp=datetime.now(),bool=False)
            first.save()
            quiz1.save()
            return render(request, "quizEditor.html",{'nameOfQuiz':nameQuiz})
        else:
            if (is_valid_uuid(nameQuiz)):
                quiz1=QuizFinal.objects.filter(code=nameQuiz)
                if(quiz1.count()!=0):
                    quiz2=quiz1[0]
                    student1=StudentFinal.objects.create(quiz=quiz2,nameOfStudent=current_user.username)
                    student1.save()
                    questions=list(QuestionFinal.objects.filter(tutor=quiz2))
                    # stud=StudentFinal.objects.filter(quiz=quiz2)
                    optionHere=[]
                    op1=questions[0].op1
                    op2=questions[0].op2
                    op3=questions[0].op3
                    op4=questions[0].op4
                    options=[op1,op2,op3,op4]
                    for i in options:
                        if(i!=None):
                            optionHere.append(i)
                    print(len(optionHere))
                    return render(request,"quizStarted.html",{"que":questions[0],"options":optionHere,"code":quiz2.code,"questionIndex":0, "timer": questions[0].questionTimer, "quizTime":quiz2.quizTimer })
                else:
                    messages.add_message(request,messages.INFO,"Enter the code Correctly!!")
                    return render(request,"createQuiz.html",{"createQuiz":"Join Quiz","NameOfTheQuiz": "Code of the Quiz", "create": "Join"})
                
            else:
                #send message code incorrect
                messages.add_message(request,messages.INFO,"Enter the code Correctly!!")
                return render(request,"createQuiz.html",{"createQuiz":"Join Quiz","NameOfTheQuiz": "Code of the Quiz", "create": "Join"})

def handleQuestionCreation(request):
    form= StudentForm
    mydict={
        'form' :form
    }
    return render(request,"questionCreator.html", context=mydict)
    
def handleMultipleChoice(request):
    if request.method=="POST":
        questionHere=request.POST.get('questionHere')
        op1Here=request.POST.get('op1Here')
        op2Here=request.POST.get('op2Here')
        op3Here=request.POST.get('op3Here')
        op4Here=request.POST.get('op4Here')

        op1Select=request.POST.get('op1Select')
        op2Select=request.POST.get('op2Select')
        op3Select=request.POST.get('op3Select')
        op4Select=request.POST.get('op4Select')

        lst=[op1Select,op2Select,op3Select,op4Select]
        opLst=[op1Here,op2Here,op3Here,op4Here]
        Ans=[]
        for i in range(len(lst)):
            if lst[i] is None:
                pass
            else:
                Ans.append(opLst[i])

        ansHere=""
        for i in Ans:
            ansHere+=i
            ansHere+=";"

        current_user=request.user
        first=AllQuizes.objects.filter(tutorName=current_user).order_by('-id')[0]
        quiz1=QuizFinal.objects.filter(tutor=first).order_by('-id')[0]
        question1=QuestionFinal.objects.create(tutor=quiz1,que=questionHere,op1=op1Here,op2=op2Here,op3=op3Here,op4=op4Here,number=1,ans=ansHere)
        question1.save()
        return render(request,"quizEditor.html",{'nameOfQuiz':quiz1.nameOfQuiz})

def subjective(request):
    return render(request, "subjective.html")
def handleSubjective(request):
    if request.method=="POST":
        questionHere=request.POST.get('questionHere')
        answerHere=request.POST.get('answerHere')

        current_user=request.user
        first=AllQuizes.objects.filter(tutorName=current_user).order_by('-id')[0]
        quiz1=QuizFinal.objects.filter(tutor=first).order_by('-id')[0]
        question1=QuestionFinal.objects.create(tutor=quiz1,que=questionHere,ans=answerHere, number=1)
        question1.save()
        return render(request,"quizEditor.html",{'nameOfQuiz':quiz1.nameOfQuiz})

def handlePoll(request):
    return render(request,"poll.html")
def handlePollCreator(request):
    if request.method=="POST":
        questionHere=request.POST.get('questionHere')
        op1Here=request.POST.get('op1Here')
        op2Here=request.POST.get('op2Here')
        op3Here=request.POST.get('op3Here')
        op4Here=request.POST.get('op4Here')

        op1Select=request.POST.get('op1Select')
        op2Select=request.POST.get('op2Select')
        op3Select=request.POST.get('op3Select')
        op4Select=request.POST.get('op4Select')
        current_user=request.user
        first=AllQuizes.objects.filter(tutorName=current_user).order_by('-id')[0]
        quiz1=QuizFinal.objects.filter(tutor=first).order_by('-id')[0]
        question1=QuestionFinal.objects.create(tutor=quiz1,que=questionHere,op1=op1Here,op2=op2Here,op3=op3Here,op4=op4Here,number=1)
        question1.save()
        return render(request,"quizEditor.html",{'nameOfQuiz':quiz1.nameOfQuiz})

def handleImport(request):
    return render(request,"importSpreadsheet.html")

def handleImportSpreadsheet(request):
    if request.method=="POST":
        QuestionFinal_resource= QuestionFinalResource()
        dataset=Dataset()
        my_uploaded_file = request.FILES['myfile']
        if not my_uploaded_file.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, "importSpreadsheet.html")
        imported_data=dataset.load(my_uploaded_file.read(), format='xlsx')
        current_user=request.user
        first=AllQuizes.objects.filter(tutorName=current_user).order_by('-id')[0]
        quiz1=QuizFinal.objects.filter(tutor=first).order_by('-id')[0]
        quizTime=0

        for i in range(len(imported_data['Question Text'])):
            if(imported_data['Question Text'][i] is not None):
                options=[]
                timer=imported_data['Time in seconds'][i]
                quizTime+=timer
                if(imported_data['Option 1'][i] is not None):
                    options.append(imported_data['Option 1'][i])
                if(imported_data['Option 2'][i] is not None):
                    options.append(imported_data['Option 2'][i])
                if(imported_data['Option 3'][i] is not None):
                    options.append(imported_data['Option 3'][i])
                if(imported_data['Option 4'][i] is not None):
                    options.append(imported_data['Option 4'][i])
                
               
                if(len(options)==0):
                    question1=QuestionFinal.objects.create(tutor=quiz1,que=(imported_data['Question Text'][i]),number=1, questionTimer=timer)
                    question1.save()
                elif len(options)==1:
                    question1=QuestionFinal.objects.create(tutor=quiz1,que=(imported_data['Question Text'][i]),op1=options[0],number=1, questionTimer=timer)
                    question1.save()
                elif len(options)==2:
                    question1=QuestionFinal.objects.create(tutor=quiz1,que=(imported_data['Question Text'][i]),op1=options[0],op2=options[1],number=1, questionTimer=timer)
                    question1.save()
                elif len(options)==3:
                    question1=QuestionFinal.objects.create(tutor=quiz1,que=(imported_data['Question Text'][i]),op1=options[0],op2=options[1],op3=options[2],number=1, questionTimer=timer)
                    question1.save()
                elif len(options)==4:
                    question1=QuestionFinal.objects.create(tutor=quiz1,que=(imported_data['Question Text'][i]),op1=options[0],op2=options[1],op3=options[2],op4=options[3],number=1, questionTimer=timer)
                    question1.save()
        quiz1.quizTimer=quizTime
        return render(request,"quizEditor.html",{'nameOfQuiz':quiz1.nameOfQuiz})

        # file=pd.read_excel(my_uploaded_file)
        # ques=list(file['Question Text'])
        # option1=list(file['Option1'])

        # current_user=request.user
        # first=AllQuizes.objects.filter(tutorName=current_user).order_by('-id')[0]
        # quiz1=QuizFinal.objects.filter(tutor=first).order_by('-id')[0]
        # for i in range(len(ques)):

        #     question1=QuestionFinal.objects.create(tutor=quiz1,que=ques[i],op1=option1[i],op2=" ",op3=" ",op4=" ",number=1)
        #     question1.save()
        
        #uploadedFile work 
        #extract questions
            # return render(request,"quizEditor.html")

def handleStartQuiz(request):
    if request.method=="POST":
        codeHere=request.POST.get('quizCheck')
        quiz1=QuizFinal.objects.filter(code=codeHere).update(bool=True)
        user=request.user
        first=AllQuizes.objects.filter(tutorName=user)
        quizes=[]
        for i in first.iterator():
            quiz2=QuizFinal.objects.filter(tutor=i)
            quizes.append(quiz2)
            quizes.reverse()
        return render(request,"indexLogged.html",{"username":user.username,"CreateQuiz":"CreateQuiz","ContentDescription":"Teacher Here!","YourQuizes":"Your Quizes","quizes":(quizes),"len":len(quizes)})

def handleEndQuiz(request):
    if request.method=="POST":
        codeHere=request.POST.get('quizCheck')
        quiz1=QuizFinal.objects.filter(code=codeHere).update(bool=False)
        user=request.user
        first=AllQuizes.objects.filter(tutorName=user)
        quizes=[]
        for i in first.iterator():
            quiz2=QuizFinal.objects.filter(tutor=i)
            quizes.append(quiz2)
        quizes.reverse()
        return render(request,"indexLogged.html",{"username":user.username,"CreateQuiz":"CreateQuiz","ContentDescription":"Teacher Here!","YourQuizes":"Your Quizes","quizes":(quizes),"len":len(quizes)})

# def handleRedirect(request):
#     if request.method=='POST':
#         nameQuiz=request.POST.get('quizCheck')
#         quiz1=QuizFinal.objects.filter(code=nameQuiz)[0]
#         stud=StudentFinal.objects.filter(quiz=quiz1)
#         return render(request,"studentLand.html",{"code":nameQuiz,"stud":stud,"nameOfQuiz":quiz1.nameOfQuiz})
    
def handleQuizStarted(request):
    return render(request,"quizStarted.html")

def handleNextQuestion(request):
    if request.method=="POST":
        code=request.POST.get('quizCheck')
        index=int(request.POST.get('questionIndex'))+1
        quiz2=QuizFinal.objects.filter(code=code)[0]
        questions=list(QuestionFinal.objects.filter(tutor=quiz2))
        # stud=StudentFinal.objects.filter(quiz=quiz2)
        if(quiz2.bool==True and index<len(questions)):
            optionHere=[]
            op1=questions[index].op1
            op2=questions[index].op2
            op3=questions[index].op3
            op4=questions[index].op4
            options=[op1,op2,op3,op4]
            for i in options:
                print(i)
                print(len(i))
                if(i!=" " and len(i)!=0):
                    optionHere.append(i)
            print(len(optionHere))
            print(questions[index].questionTimer)
            return render(request,"quizStarted.html",{"que":questions[index],"options":optionHere,"code":code,"questionIndex":index, "timer": questions[index].questionTimer})
        else:
            return render(request,"index.html")