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

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            #'error_message': "You didn't select a choice.",
            'error_message': "No seleccionaste una opción.",
        })
    else:
        selected_choice.respuesta
        #selected_choice.votes += 1
        #selected_choice.save()
        c = {}
        for opcion in opciones:
            if respuesta:
                c[opcion] = question.id in elegidos
            else:
                c[opcion] = question.id not in elegidos
        # Always return an HttpResponseRedirect after successfully dealing
        # Siempre devolver un HttpResponseRedirect después de tratar con éxito
        # with POST data. This prevents data from being posted twice if a
        # con datos POST. Esto evita que los datos se publiquen dos veces si
        # user hits the Back button.
        # usuario pulsa el botón Atrás.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        print('selected_choice %s'%(selected_choice))
    #return HttpResponse("You're voting on question %s." % question_id)

