from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage

from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    limit = 10
    questions = Question.objects.new()
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'index.html',
                  {'title': 'new questions', 'paginator': paginator, 'questions': page.object_list, 'page': page})


def popular(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    limit = 10
    questions = Question.objects.popular()
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'index.html',
                  {'title': 'popular questions', 'paginator': paginator, 'questions': page.object_list, 'page': page})


def question(request, idk):
    q = get_object_or_404(Question, id=idk)
    return render(request, 'question.html', {'question': q})
