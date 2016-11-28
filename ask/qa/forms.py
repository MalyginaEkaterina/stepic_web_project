from django import forms
from models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    
    def save(self):
      try:
        user = User.objects.get(username='katty')
      except User.DoesNotExist:
        user = User.objects.create_user('katty', email='katty@ya.ru', password='katty')
      question = Question(author=user,**self.cleaned_data)
      question.save()
      return question
    
class AnswerForm(forms.Form):    
    text = forms.CharField() 
    question = forms.IntegerField(widget=forms.HiddenInput)
    
    def clean_question(self):
      return Question.objects.get(id = self.cleaned_data['question'])
    
    def save(self):
      try:
        user = User.objects.get(username='a_katty')
      except User.DoesNotExist:
        user = User.objects.create_user('a_katty', email='a_katty@ya.ru', password='a_katty')
      answer = Answer(author=user, **self.cleaned_data)
      answer.save()
      return answer
