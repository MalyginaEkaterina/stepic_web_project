from django import forms
from models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    
    def save(self,user):
      question = Question(author=user,**self.cleaned_data)
      question.save()
      return question
    
class AnswerForm(forms.Form):    
    text = forms.CharField() 
    question = forms.IntegerField(widget=forms.HiddenInput)
    
    def clean_question(self):
      return Question.objects.get(id = self.cleaned_data['question'])
    
    def save(self,user):
      answer = Answer(author=user, **self.cleaned_data)
      answer.save()
      return answer

class SignupForm(forms.Form):    
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) 
    
    def save(self):
      user = User.objects.create_user(self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])  
      return user

class LoginForm(forms.Form):    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 
