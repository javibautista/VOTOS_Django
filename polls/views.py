from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from django.shortcuts import render
## tercer agregacion
from django.urls import reverse
# segundo cambio
from .models import Choice, Question
#cuarto cambio
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Devuelve las últimas 5 preguntas publicadas."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def results(request, question_id):
    # tercer agregacion tutorial4
    question = get_object_or_404(Question, pk=question_id)
    #choice = get_object_or_404(Choice, pk=question_id)
    opciones = question.choice_set.all()
    elegidas = question.choice_set.filter(pk__in=request.POST.getlist('choice'))
    c = {}
    for opcion in opciones:
        if respuesta:
            c[opcion] = question.id in elegidas
        else:
            c[opcion] = question.id not in elegidas

    print('QUESTION %s'%(question))
    print('OPCIONES %s'%(opciones))
    print('ELEGIDOS %s'%(elegidas))


