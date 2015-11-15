# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_id', models.CharField(default=True, max_length=30)),
                ('answerer_id', models.CharField(default=True, max_length=30)),
                ('question_id', models.CharField(default=True, max_length=30)),
                ('content', models.CharField(default=True, max_length=1024)),
                ('answer_time', models.TimeField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(default=True, max_length=30, serialize=False, primary_key=True)),
                ('course_name', models.CharField(default=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('course_id', models.CharField(default=True, max_length=30, null=True)),
                ('student_id', models.CharField(default=True, max_length=30, null=True)),
                ('title', models.CharField(default=True, max_length=1024, null=True)),
                ('post_time', models.CharField(default=True, max_length=1024, null=True)),
                ('content', models.CharField(default=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_id', models.CharField(default=b'007', max_length=30, serialize=False, primary_key=True)),
                ('student_id', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(max_length=1, null=True, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('year_in_school', models.CharField(max_length=2, null=True, choices=[(b'UN', b'UnderGraduate'), (b'GR', b'Graduate')])),
                ('major', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.CharField(default=b'123', max_length=30)),
                ('course_id', models.CharField(default=b'123', max_length=30)),
            ],
        ),
    ]
