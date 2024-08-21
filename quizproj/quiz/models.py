from django.db import models
from datetime import date
# Create your models here.
class QuizQuestions(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(blank=False,max_length=25)
    data=models.JSONField()
    url=models.CharField(blank=False, max_length=200)

class QuizScores(models.Model):
    id=models.AutoField(primary_key=True)
    code=models.IntegerField(blank=False)
    author=models.CharField(blank=False, max_length=50)
    name=models.CharField(blank=False, max_length=50)
    score=models.IntegerField()
    total=models.IntegerField()
    date=models.DateField(default=date.today())