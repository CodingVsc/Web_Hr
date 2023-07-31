from rest_framework import generics, permissions

from django_filters.rest_framework import DjangoFilterBackend


from .models import Job, Grade, HrQuestions, TechQuestions
from .serializers import JobSerializer, GradeSerializer, HrQuestionsSerializer, TechQuestionsSerializer
from .paginators import QuestionPagination
from .filters import JobFilter


class ListJobApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = JobFilter


class ListGradeApiView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class ListHrQuestionsApiView(generics.ListAPIView):
    queryset = HrQuestions.objects.all()
    serializer_class = HrQuestionsSerializer
    pagination_class = QuestionPagination


class ListTechQuestionsApiView(generics.ListAPIView):
    serializer_class = TechQuestionsSerializer
    pagination_class = QuestionPagination

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        grade_id = self.kwargs['grade_id']

        return TechQuestions.objects.filter(job_id=job_id, grade_id=grade_id)





