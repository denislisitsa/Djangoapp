from django.http import HttpResponseBadRequest, HttpResponse
from random import randint
from .models import Student


def generate_student(request):
    if request.method == 'POST' or request.method == 'GET':
        first_name = 'John'
        last_name = 'Doe'
        age = randint(18, 30)

        student = Student(first_name=first_name, last_name=last_name, age=age)
        student.save()

        return HttpResponse("Студент создан,все хорошо.")
    else:
        return HttpResponseBadRequest("Неправильный метод")


def generate_students(request):
    if request.method == 'GET':
        count = request.GET.get('count', None)
        if count is None or not count.isdigit() or int(count) <= 0 or int(count) > 100:
            return HttpResponseBadRequest("Недопустимое значение.")
        for i in range(int(count)):
            first_name = 'John'
            last_name = 'Doe'
            age = randint(18, 30)

            student = Student(first_name=first_name, last_name=last_name, age=age)
            student.save()

        return HttpResponse(f"{count} количество созданных студентов.")
    else:
        return HttpResponseBadRequest("Неправильный метод.")
