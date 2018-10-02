"""
AUTHOR      :   Robert James Patterson
DATE:       :   10/02/2018
SYNOPSIS    :   Working thru the 'docs.djangoproject.com' tutorial
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)


def results(request, question_id):
    response = "You are looking ar the results for question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You are voting on question %s."
    return HttpResponse(response % question_id)





