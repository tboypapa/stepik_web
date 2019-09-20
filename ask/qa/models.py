from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="q_author", null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_likes")


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name="q_answers", null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, related_name="a_author", null=True, on_delete=models.SET_NULL)
