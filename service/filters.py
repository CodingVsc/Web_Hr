from django_filters import rest_framework as filters

from .models import Job


class JobFilter(filters.FilterSet):
    job_type = filters.CharFilter(field_name='job_type', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['job_type']