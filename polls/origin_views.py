"""
from django.shortcuts import render

# Create your views here.
"""
#from django.http import HttpResponse
# tercer cambio
#from django.template import loader
###tercer agregacion####
#from django.http import HttpResponse, HttpResponseRedirect
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
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #### cambio que muestra lo mismo pero render es el mas usado ####
    #### import que no irian en ejemplo render ####
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    ##############################
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")


# Leave the rest of the views (detail, results, vote) unchanged
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # agregado para error
    ##try:
        ##question = Question.objects.get(pk=question_id)
    ##except Question.DoesNotExist:
        ##raise Http404("Question does not exist")
    ##return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    #tutorial4
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
"""

def vote(request, question_id):
    # tercer agregacion tutorial4
    question = get_object_or_404(Question, pk=question_id)

    request.POST
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
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)
