from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:6]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    #try:
    #    question=Question.objects.get(pk=question_id)
    #except:
    #    raise Http404("Question does not exists")
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response="You're looking at the result of the question %s."
    return HttpResponse(response%question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s."%question_id)




