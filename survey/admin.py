from django.contrib import admin
from .models import Survey, Question, Answer, Vote


class AdminSurvey(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'finish_date', 'description']
    list_editable = ['description']


class AdminQuestion(admin.ModelAdmin):
    list_display = ['type', 'content']
    list_editable = ['content']

admin.site.register(Survey, AdminSurvey)
admin.site.register(Question, AdminQuestion)
admin.site.register(Answer)
admin.site.register(Vote)
