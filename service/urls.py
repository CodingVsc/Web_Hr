from django.urls import path

from .views import (ListJobApiView, ListHrQuestionsApiView,
                   ListGradeApiView, ListTechQuestionsApiView)


urlpatterns = [
    path('jobs/', ListJobApiView.as_view()),
    path('grades/', ListGradeApiView.as_view()),
    path('hr-questions/', ListHrQuestionsApiView.as_view()),
    path('tech-questions/<int:job_id>/<int:grade_id>/', ListTechQuestionsApiView.as_view()),
]
