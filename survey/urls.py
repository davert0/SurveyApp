from django.conf.urls import url
from django.urls import include
from .views import SurveyViewSet, QuestionViewSet, VoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('surveys', SurveyViewSet)
router.register('questions', QuestionViewSet)
router.register('votes', VoteViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]