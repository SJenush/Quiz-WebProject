from quiz.models import QuizQuestions, QuizScores


def CalculateScore(request,ans):
    score=0
    sel_ans=[]
    for i in range(1,len(ans)+1):
        sel_ans.append(request.POST.get(f'q{i}'))
        if sel_ans[i-1]==ans[i-1]:
            score+=1
    print(sel_ans)
    return score,len(ans)

def AddScoreToTable(link,score,total,request):
    record=QuizQuestions.objects.get(url=link)
    new_score=QuizScores(code=record.id,author=record.username,score=score,total=total,name=request.user.username)
    new_score.save()
    print("Score added successfully")