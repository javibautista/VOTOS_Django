#agregado2
import datetime

from django.db import models
#agregado2
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Fech de Publicación')
    #agregado1
    def __str__(self):
        return self.question_text
    #agregado2
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    #correcto = models.BooleanField(default=False)
    #agregado1
    def __str__(self):
        return self.choice_text

