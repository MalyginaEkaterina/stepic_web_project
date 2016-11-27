from django.shortcuts import render
from django.http import HttpResponse 
from django.core.paginator import Paginator
from django.http import Http404
from models import Question, Answer
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
    return HttpResponse('OK')
    
def main_page(request):
    try:
      page = int(request.GET.get('page',1))
    except ValueError:
      raise Http404
    limit = 10
    questions = Question.objects.new()
    paginator = Paginator(questions,limit)
    paginator.baseurl = reverse('main_page')+'?page='
    try:
      page = paginator.page(page)
    except EmptyPage:
      page = paginator.page(paginator.num_pages)
    return render(request,'main_page.html', {'questions': page.object_list, 'paginator': paginator, 'page': page,})
    
def question_page(request, id):
    try:
      question = Question.objects.get(id = id)
    except Question.DoesNotExist:
      raise Http404
      
    try:
      answers = question.answer_set.all()
    except Answer.DoesNotExist:
      answers = None
    return render(request,'question_page.html', {'question': question, 'answers': answers,})

def popular_questions(request):
    try:
      page = int(request.GET.get('page',1))
    except ValueError:
      raise Http404
    limit = 10
    questions = Question.objects.popular()
    paginator = Paginator(questions,limit)
    paginator.baseurl = reverse('popular_questions')+'?page='
    try:
      page = paginator.page(page)
    except EmptyPage:
      page = paginator.page(paginator.num_pages)
    return render(request,'popular_page.html', {'questions': page.object_list, 'paginator': paginator, 'page': page,})

