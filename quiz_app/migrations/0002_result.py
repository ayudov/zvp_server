# Generated by Django 2.1.1 on 2018-09-25 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0002_auto_20180903_1120'),
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.TextField(editable=False, verbose_name='Відповіді студента')),
                ('date_time_stamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата та час складання тесту')),
                ('student', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='control_panel.Student', verbose_name='Студент')),
                ('test', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.Quiz', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результати',
                'db_table': 'Results',
            },
        ),
    ]
