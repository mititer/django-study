from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
import  logging
from django.views import generic
from django.utils import timezone

# Create your views here.
def index(request):
    '''
    hard coded index content
    '''
    # return HttpResponse('Hello world! You are at the polls index.')
    '''
    hard coded view content with data
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    '''

    '''
    # use template directly
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    '''

    # use template with shortcut style ( indirectly)
    ''''''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # hard code
    # return HttpResponse(f"You're looking at question {question_id}")
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404(f"Question {question_id} does not exist.")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Rediplay the question voting form
        ctx = {
            'question': question,
            'error_message': "You didn't select a choice",
        }
        return render(request, 'polls/detail.html', ctx)
    except:
        ctx = {
            'question': question,
            'error_message': "unexpected error",
        }
        logging.error("error +++++")
        return render(request, 'polls/detail.html', ctx)
    #else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        '''Return the last five published questions.'''
        # return Question.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'