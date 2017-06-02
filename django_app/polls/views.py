
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404

from .models import Question, Choice


def index(request):
    # latest_question_list = Question.objects.order_by('pub_date')[:5]
    # latest_question_list 라는 키로 위 쿼리셋을 전달
    # get_list_or_404 사용...쿼리셋을 인자로 준다.
    latest_question_list = get_list_or_404(Question.objects.order_by('pub_date')[:5])
    # polls/index.html 를 이용해 render 한결과를 리턴
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')
    # else:
    # get_object_
    question = get_object_or_404(Question, pk=question_id)
    # question.choice_set. (아래와 같다)
    # Choice.objects.filter(question=question).
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse('results of question {}'.format(question_id))


def vote(request, question_id):
    # request 의 method가 post 방식일때, 전달받은 데이터 중 'choice' 키에 해당하는 값을 HttpResponse 에 적절히 돌려준다.
    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            # choice 키에 해당하는 Choice 인스턴스의 vote 값을 1증가시키고 데이터베이스에 반영
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice"
            )
            return redirect('polls:detail', question_id)
        # 이후 results 페이지로 redirect
        return redirect('polls:results', question_id)
    else:
        return HttpResponse("You're voting")

