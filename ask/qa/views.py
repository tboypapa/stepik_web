from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage

from .models import Question
from .forms import AskForm, AnswerForm


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


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def question(request, idk):
    q = get_object_or_404(Question, id=idk)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': q.id})

    return render(request, 'question.html', {'question': q, 'form': form})
