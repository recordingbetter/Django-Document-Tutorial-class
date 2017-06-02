from django.contrib import admin
# 내부 모델을 참조할 경우 상대경로를 쓴다.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ('pub_date', 'question_text')
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently',
    )
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = (ChoiceInline,)


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceInline)
