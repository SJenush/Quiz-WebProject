from django.shortcuts import render,redirect
from quiz.questions import CreateContext,GetAnswers
from quiz.scores import CalculateScore
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from quiz.login_register import register as auth_register
# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required(login_url='login',redirect_field_name='redirectFrom')
def quizPage(request):
    if request.method == 'POST':
        score,total=CalculateScore(request,GetAnswers())
        return redirect(f'/score/?score={score}&total={total}')
    context=CreateContext('QuizPage')
    return render(request,'quiz_page.html',context)
def quizScore(request):
    if request.method == 'GET':
        point=request.GET.get('score')
        total=request.GET.get('total')
        context=CreateContext('ViewScore')
        context["score"]=point
        context["total"]=total
        return render(request,'quiz_score.html',context)
    else:return redirect('quizPage')
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