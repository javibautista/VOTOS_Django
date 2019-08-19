"""
from django.db import forms
from django import forms
from .models import Choice, Question
class Question(forms.Modelform):
    #quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Fecha de Publicación')
    #agregado1
    def __str__(self):
        return self.question_text
    #agregado2
    #def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(forms.Modelform):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)####, related_name='answers')
    choice_text = models.CharField(max_length=100)##'Answer', max_length=100)
    #votes = models.IntegerField(default=0)
    votes = models.BooleanField(default=False)
    #op_correcta = models.BooleanField('Correct answer', default=False)
    #agregado1
    def __str__(self):
        return self.choice_text
"""
