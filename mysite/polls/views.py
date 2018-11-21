from django.shortcuts import render, redirect
from.models import *

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions' : questions})


def show_question(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'question.html', {'question' : question})

def show_results(request, question_id):
    return redirect('index')