from django.shortcuts import render
from django.http import HttpResponse 
from django.core.paginator import Paginator
from django.http import Http404
from models import Question, Answer
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login

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
    
    if request.method == 'POST':
      form = AnswerForm(request.POST)
      if form.is_valid():
        answer = form.save(request.user)
        url = '/question/' + str(id) + '/'
        return HttpResponseRedirect(url)
    else:
      form = AnswerForm({'question': id})
      
    return render(request,'question_page.html', {'question': question, 'answers': answers, 'form': form,})

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
    
def ask_page(request):
    if request.method == 'POST':
      form = AskForm(request.POST)
      if form.is_valid():
        question = form.save(request.user)
        url = '/question/'+str(question.id)+'/'
        return HttpResponseRedirect(url)
    else:
      form = AskForm()
    return render(request,'question_add.html', {'form': form,})
    
def signup(request):
    if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
        user = form.save()
        login(request, user)
        url = '/'
        return HttpResponseRedirect(url)
    else:
      form = SignupForm()
    return render(request,'signup.html', {'form': form,})

def login_page(request):
    if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
          if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
    else:
      form = LoginForm()
    return render(request,'login.html', {'form': form,})
