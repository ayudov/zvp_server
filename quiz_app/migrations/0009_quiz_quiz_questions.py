# Generated by Django 2.0.2 on 2018-03-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0008_auto_20180313_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_questions',
            field=models.ManyToManyField(help_text='Питання до тесту', to='quiz_app.Question', verbose_name='Питання'),
        ),
    ]