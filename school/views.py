from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    object_list = Student.objects.all().order_by('group')
    template = 'school/students_list.html'
    context = {
        'object_list': object_list
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

# {% for teacher in student.teachers.all %}
# <p>{{ teacher.name }}: {{ teacher.subject }}
# {% for student in object_list %}
#     <li>{{ student.name }} {{ student.group }} <br> Преподаватель: {{ student.teacher.name }} {{ student.teacher.subject }}</li>
#   {% endfor %}
