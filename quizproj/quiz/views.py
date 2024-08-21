from django.shortcuts import render,redirect
from quiz.questions import CreateContext,GetAnswers,GetCustomAnswers
from quiz.scores import AddScoreToTable, CalculateScore
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from quiz.login_register import register as auth_register
from quiz.CreateQuizQns import addQuestions
from quiz.getQuizes import getAllQuestions
from quiz.submissions import GetDetails
# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required(login_url='login',redirect_field_name='redirectFrom')
def ViewQuiz(request):
    data=getAllQuestions(request)
    context={"quiz":data,"user":request.user.username}
    return render(request,'view_all_quiz.html',context)
def quizPage(request):
    link=request.GET.get('quizLink')
    if request.method == 'POST':
        if link is not None:
            score,total=CalculateScore(request,GetCustomAnswers(link))
            AddScoreToTable(link,score,total,request)
            return redirect(f'/score/?quizLink={link}&score={score}&total={total}')
        else:
            score,total=CalculateScore(request,GetAnswers())
        return redirect(f'/score/?score={score}&total={total}')
    if link is not None:
        context=CreateContext(request,'QuizPage',True)
        return render(request,'quiz_page.html',context)
    context=CreateContext(request,'QuizPage',False)
    return render(request,'quiz_page.html',context)
def ViewSubmissions(request):
    link=request.GET.get('quizLink')
    if link is not None:
        scores=GetDetails(link)
        context={"details":scores}
        return render(request,'view_submissions.html',context)
    return render(request,'view_submissions.html')
def quizScore(request):
    if request.method == 'GET':
        point=request.GET.get('score')
        total=request.GET.get('total')
        link=request.GET.get('quizLink')
        if link is not None:
            context=CreateContext(request,'ViewScore',True)
            context["score"]=point
            context["total"]=total
            return render(request,'quiz_score.html',context)
        context=CreateContext(request,'ViewScore',False)
        context["score"]=point
        context["total"]=total
        return render(request,'quiz_score.html',context)
    else:return redirect('quizPage')
@login_required(login_url='login',redirect_field_name='redirectFrom')
def CreateQuiz(request):
    if request.method=='POST':
        url=addQuestions(request)
        return redirect(f'/GenerateLinkPage?quizLink={url}')
    return render(request,'createQuiz.html')
def GenerateLinkPage(request):
    url=request.GET.get('quizLink')
    context={"url":url,}
    return render(request,'generate_link.html',context)
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        redirect_url=request.GET.get('redirectFrom')
        if redirect_url is None:
            redirect_url='/'
        name=request.POST["username"]
        pwd=request.POST["password"]
        print(name,pwd)
        user=authenticate(username=name,password=pwd)
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect(redirect_url)
        else:
            err='*Invalid Creditionals'
            context={
                'error_msg':err
            }
            return render(request,'login.html',context)
    return render(request,'login.html')
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        flag,context= auth_register(request)
        if(flag):
            return redirect('/')
        else:
            return render(request,'register.html',context=context)
    return render(request,'register.html')
def logoutPage(request):
    logout(request)
    return redirect('/')