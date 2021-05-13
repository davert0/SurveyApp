from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Survey, Question, Vote
from .serializers import SurveySerializer, QuestionSerializer, VoteSerializer
from .permissions import SurveyPermission, QuestionPermission
from .filters import VoteFilter


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (SurveyPermission,)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = (DjangoFilterBackend, )
    http_method_names = ('get', 'post')
    filterset_class = VoteFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (QuestionPermission, )