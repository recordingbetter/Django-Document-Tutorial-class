from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    # latest_question_list 라는 키로 위 쿼리셋을 전달
    # polls/index.html 를 이용해 render 한결과를 리턴
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse('questions {}'.format(question_id))


def results(request, question_id):
    return HttpResponse('results of question {}'.format(question_id))


def vote(request, question_id):
    return HttpResponse('voting on question {}'.format(question_id))
