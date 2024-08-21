from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login as auth_login
def register(request):
    if request.method=='POST':
        redirect_url=request.GET.get('redirectFrom')
        username=request.POST["username"]
        email=request.POST["email"]
        pwd=request.POST["password"]
        con_pwd=request.POST["con_password"]
        if pwd != con_pwd:
            context={"error":"*Passwords don't match"}
            return False,context
        if User.objects.filter(username=username).exists():
            context={"error":'*Username already taken'}
            return False,context
        if User.objects.filter(email=email).exists():
            context={"error":'*Already an account is registered with this email'}
            return False,context
        User.objects.create(username=username,email=email,password=make_password(pwd))
        user=authenticate(username=username,password=pwd)
        auth_login(request,user)
        context={"error":''}
        return True,context
    return False,{"error":''}

def SetSessionVariables(user,request):
    user_t=User.objects.get(username=user.username)
    