# Generated by Django 2.0.2 on 2018-03-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0011_question_question_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_answers',
        ),
        migrations.AddField(
            model_name='question',
            name='question_fifth_answer_content',
            field=models.CharField(default=1, help_text='Варіант відповіді під літерою А', max_length=450, verbose_name='Д'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_fifth_answer_state',
            field=models.BooleanField(default=False, help_text='Показчик чи є відповідь вірною', verbose_name='Правильна відповідь'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_first_answer_content',
            field=models.CharField(default=1, help_text='Варіант відповіді під літерою А', max_length=450, verbose_name='А'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_first_answer_state',
            field=models.BooleanField(default=False, help_text='Показчик чи є відповідь вірною', verbose_name='Правильна відповідь'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_fourth_answer_content',
            field=models.CharField(default=1, help_text='Варіант відповіді під літерою А', max_length=450, verbose_name='Г'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_fourth_answer_state',
            field=models.BooleanField(default=False, help_text='Показчик чи є відповідь вірною', verbose_name='Правильна відповідь'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_second_answer_content',
            field=models.CharField(default=1, help_text='Варіант відповіді під літерою А', max_length=450, verbose_name='Б'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_second_answer_state',
            field=models.BooleanField(default=False, help_text='Показчик чи є відповідь вірною', verbose_name='Правильна відповідь'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_third_answer_content',
            field=models.CharField(default=1, help_text='Варіант відповіді під літерою А', max_length=450, verbose_name='В'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_third_answer_state',
            field=models.BooleanField(default=False, help_text='Показчик чи є відповідь вірною', verbose_name='Правильна відповідь'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
