from django.contrib import admin
from .models import *

admin.site.site_title = 'Кафедра Військової Підготовки. Адміністрування'
admin.site.site_header = 'Кафедра Військової Підготовки. Адміністрування'


class QuestionLayout(admin.ModelAdmin):

    list_display = (
        'question_discipline',
        'question_content',
        'get_quizzes',
        'link'
    )

    list_display_links = ('link', )

    list_editable = (
        'question_discipline',
        'question_content',
    )


class QuizLayout(admin.ModelAdmin):
    list_display = (
        'quiz_title',
        'quiz_description',
        'quiz_discipline',
        'quiz_single_attempt',
        'link'
    )

    list_display_links = ('link', )

    list_editable = (
        'quiz_title',
        'quiz_description',
        'quiz_discipline',
        'quiz_single_attempt',
    )


class AnswerLayout(admin.ModelAdmin):
    list_display = (
        'answer_title',
        'answer_question',
        'answer_is_correct',
        'link'
    )

    list_display_links = ('link', )

    list_editable = (
        'answer_title',
        'answer_question',
        'answer_is_correct'
    )


admin.site.register(Question, QuestionLayout)
admin.site.register(Quiz, QuizLayout)
admin.site.register(Answer, AnswerLayout)
