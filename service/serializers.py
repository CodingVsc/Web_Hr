from rest_framework import serializers

from .models import *


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('job_type',)


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('grade_type',)


class HrQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HrQuestions
        fields = ('question', 'answer')


class TechQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechQuestions
        fields = ('question', 'answer')
