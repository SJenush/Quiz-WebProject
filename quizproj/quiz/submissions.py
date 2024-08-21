from quiz.models import QuizQuestions, QuizScores


def GetDetails(link):
    record=QuizQuestions.objects.get(url=link)
    details=QuizScores.objects.filter(code=record.id).order_by('-score')
    return details