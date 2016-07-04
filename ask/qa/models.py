from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM qa_question q ORDER BY q.added_at DESC")
        last_questions = cursor.fetchall()
        return last_questions

    def popular(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM qa_question q ORDER BY q.rating DESC")
        popular_questions = cursor.fetchall()
        return popular_questions

class Question(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,related_name='question_author')
    likes = models.ManyToManyField(User,related_name='question_like')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField() 
    added_at = models.DateField() 
    question = models.ForeignKey(Question) 
    author = models.ForeignKey(User,related_name='+') 
# Create your models here.
