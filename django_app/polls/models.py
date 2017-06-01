from django.db import models


class Question(models.Model):
    question_text = models.CharField('질문내용', max_length = 200)
    pub_date = models.DateTimeField('발행일자')


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name = '해당 질문', on_delete = models.CASCADE)
    choice_text = models.CharField('선택내용', max_length = 200)
    votes = models.IntegerField('총 투표수', default = 0)
