def CalculateScore(request,ans):
    score=0
    sel_ans=[]
    for i in range(1,len(ans)+1):
        sel_ans.append(request.POST.get(f'q{i}'))
        if sel_ans[i-1]==ans[i-1]:
            score+=1
    print(sel_ans)
    return score,len(ans)
    