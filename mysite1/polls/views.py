from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from django.template import loader, RequestContext

from .models import Question

# creating views here
def index(request):
    latest_questions=Question.objects.order_by('-pub_date')[:5]
    # output=", ".join(q.questionText for q in latest_questions)
    # return HttpResponse(output)
    # template=loader.get_template('polls/index.html')
    # context={
    #
    #    'latest_questions':latest_questions
    # }
    # return HttpResponse(template.render(context))
    context = {'latest_questions':latest_questions}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
   # return  HttpResponse("This is the details view of question:%s" %question_id)

def result(request,question_id):
    return  HttpResponse("These are the result of questions:%s" %question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})

def vote(request,question_id):
    # return  HttpResponse("Vote on questions:%s" %question_id)
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice=question.choice_set.get(pk= request.POST['choice'])
    except:
        return render(request,'polls:detail.html', {'question':question,'error_message': " please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))