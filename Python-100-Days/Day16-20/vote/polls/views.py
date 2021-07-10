from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect

from polls.models import Subject, Teacher

from django.http import JsonResponse


def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


def praise_or_criticize(request):
    """
    好评
    """
    try:
        tno = int(request.GET.get("tno"))
        teacher = Teacher.objects.get(no=tno)
        if request.path.startwith('/praise'):
            teacher.good_count += 1
            count = teacher.good_count
        else:
            teacher.bad_count += 1
            count = teacher.bad_count
        teacher.save()
        data = {'code': 20000, 'msg': '操作成功', 'count': count}
    except (ValueError, Teacher.DoesNotExist):
        data = {'code': -1, 'msg': '操作失败'}
    return JsonResponse(data)


def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    return render(request, 'login.html', {'hint': hint})
