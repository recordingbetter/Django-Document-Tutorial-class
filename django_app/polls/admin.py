from django.contrib import admin
# 내부 모델을 참조할 경우 상대경로를 쓴다.
from .models import Question

admin.site.register(Question)