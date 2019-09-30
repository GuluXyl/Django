from django.db import models

# Create your models here.


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    detailDesc = models.CharField(max_length=300)
    answerCount = models.IntegerField(max_length=10)
    lastModifiled = models.DateTimeField(auto_now=True)


class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    ansContent = models.CharField(max_length=300)
    ansDate = models.DateTimeField(auto_now=True)
    qid = models.ForeignKey(to='Questions', to_field='id', on_delete=models.CASCADE)
