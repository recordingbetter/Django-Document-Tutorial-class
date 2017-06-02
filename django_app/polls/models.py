from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('질문내용', max_length = 200)
    pub_date = models.DateTimeField('발행일자')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '발행?'


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name = '해당 질문', on_delete = models.CASCADE)
    choice_text = models.CharField('선택내용', max_length = 200)
    votes = models.IntegerField('총 투표수', default = 0)

    def __str__(self):
        return self.choice_text
