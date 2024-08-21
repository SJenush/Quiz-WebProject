import random
from cryptography.fernet import Fernet

from quiz.models import QuizQuestions
key=Fernet.generate_key()
cipher=Fernet(key)
def addQuestions(request):
    if request.method=='POST':
        qns=request.POST.getlist('q[]')
        title=request.POST.get('title')
        ans=[]
        op=[]
        op_count=4
        l=0
        tmp=[]
        answers=[]
        all_opts=request.POST.getlist('options[]')
        q_count=len(qns)
        for i in range(len(all_opts)):
            if i%op_count==0 and i!=0:
                op.append(tmp)
                tmp=[all_opts[i]]
            else:
                tmp.append(all_opts[i])
        for key ,value in request.POST.items():
            if key.startswith('ans'):
                ans.append(int(value))
        op.append(tmp)
        
        for i in range(len(op)):
            n=ans[i]
            val=op[i][n]
            print(val)
            answers.append(val)
        print(qns)
        print(op)
        url=GenerateLink(request)
        print(answers)
        data={
            "title":title,
            "questions":qns,
            "options":op,
            "answers":answers,
        }
        AddToDatabase(request.user.username,data,url)
        return url
def AddToDatabase(name,data,url):
    record=QuizQuestions(username=name,data=data,url=url)
    record.save()
    print("Record saved successfully!")
def GenerateLink(request):
    txt=random.randint(1200,50000)
    msg=request.user.username+str(txt)
    url=cipher.encrypt_at_time(msg.encode(),txt)
    link=str(url)
    return link