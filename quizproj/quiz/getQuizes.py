
from quiz.models import QuizQuestions


def getAllQuestions(request):
    records=QuizQuestions.objects.all().order_by('-id')
    return records