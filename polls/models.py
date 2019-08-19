import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    #quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField('Question,question_text', max_length=100)
    #guarda pub_date con tiempo para que views.py devuelva las ultimas 5 declarado en class IdexView
    pub_date = models.DateTimeField('Fecha de Publicación models.py')
    #agregado1
    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)####, related_name='answers')
    choice_text = models.CharField('Answer', max_length=100)
    #votes = models.IntegerField(default=0)
    #votes ahora es respuesta y siempre sera false a menos que se cambie en otro codigo
    respuesta = models.BooleanField('Correct answer, classChoice,respuesta', default=False)
    #op_correcta = models.BooleanField('Correct answer', default=False)
    #agregado1
    def __str__(self):
        return self.choice_text


