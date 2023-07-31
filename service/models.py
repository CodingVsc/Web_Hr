from django.db import models


class HrQuestions(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ')

    class Meta:
        verbose_name = 'Hr вопрос'
        verbose_name_plural = 'Hr вопросы'


class Job(models.Model):
    job_type = models.CharField('Название работы', max_length=50)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.job_type


class Grade(models.Model):
    grade_type = models.CharField('Грейд', max_length=30)

    class Meta:
        verbose_name = 'Грейд'
        verbose_name_plural = 'Грейды'

    def __str__(self):
        return self.grade_type


class TechQuestions(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ')
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='jobs', verbose_name='Работа')
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grades', verbose_name='Грейд')

    class Meta:
        verbose_name = 'Технический вопрос'
        verbose_name_plural = 'Технические вопросы'