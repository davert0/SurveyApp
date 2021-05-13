from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True, )
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Question(models.Model):

    class Type:
        COMMON_TXT = 'Common_txt'
        SINGLE_CHOICE = 'Single_choice'
        MULTI_CHOICE = 'Multi_choice'

        Choices = (
            (MULTI_CHOICE, 'Common_txt'),
            (SINGLE_CHOICE, 'Single_choice'),
            (COMMON_TXT, 'Multi_choice')
        )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)

    type = models.CharField(max_length=13, choices=Type.Choices, default=Type.COMMON_TXT)

    def __str__(self):
        return self.content


class Choice(models.Model):

    question = models.ForeignKey(Question, related_name='Choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=64, default='Enter value')

    def __str__(self):
        return self.text


class Vote(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=timezone.now(), editable=False)

    def __str__(self):
        return self.survey


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

    class Meta:
        unique_together = ("question", "user")
