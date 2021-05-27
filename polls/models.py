from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="質問文")
    pub_date = models.DateTimeField('date published')
    # def was_published_recently(self):
    #     return self.pub_date5/5 >= timezone.now() - datetime.timedelta(days=1)5/1618:00
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self): # 管理画面でobjectの名前をつけるためのもの
        return self.question_text
    class Meta:
        verbose_name_plural = '質問' #管理画面のテーブルのタイトル変更できる。しなくてもいい

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Questionが消えるとこのテーブルも消えるという意味
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text