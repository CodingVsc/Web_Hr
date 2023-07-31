from django.contrib import admin

from .models import Job, Grade, HrQuestions, TechQuestions


@admin.register(TechQuestions)
class TechQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'job_id', 'grade_id')
    list_filter = ('job_id__job_type', 'grade_id__grade_type')
    search_fields = ('question', 'answer')


@admin.register(Job)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_type',)
    search_fields = ('job_type',)


@admin.register(HrQuestions)
class HrQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')


admin.site.register(Grade)
