# Generated by Django 2.0.2 on 2018-04-24 09:43

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0004_remove_student_student_quizzes'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_quizzes',
            field=picklefield.fields.PickledObjectField(default=1, editable=False),
            preserve_default=False,
        ),
    ]
