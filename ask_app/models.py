# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(User):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Тег')
    questions = models.ManyToManyField('Question')


class Like(models.Model):
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    like_date_time = models.DateTimeField(auto_now_add=True)
    #like_target = models.ForeignKey('LikeTarget', on_delete=models.CASCADE)
    #две модели лайков для вопросов и ответов
    #две связи к вопросу и к ответу одна из них нулл

class LikeTarget(models.Model):
    pass


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Заголовок вопроса')
    text = models.TextField(verbose_name=u'Тело вопроса')
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    creation_date_time = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    
    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'
    
    def __str__(self):
        return "%s: \n\t%s" % (self.title, self.text)


class Answer(models.Model):
    text = models.TextField(verbose_name=u'Тело ответа')
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    creation_date_time = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    
    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'
    
    def __str__(self):
        return str(self.id) + ' ' + self.text
