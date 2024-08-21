from django.contrib import admin
from quiz.models import QuizQuestions
# Register your models here.
class QuizQn(admin.ModelAdmin):
    list_display=("id","username","data","url")
admin.site.register(QuizQuestions,QuizQn)