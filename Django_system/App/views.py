import datetime


from django.http import request
from django.shortcuts import render,redirect
from App.models import Questions,Answers


def index(request):
    text_all = Questions.objects.all()
    return render(request, 'index.html', {'text_all': text_all})


def questions(request):
    if request.method == 'POST':
        test_one = request.POST.get('question_one')
        test_two = request.POST.get('question_two')
        if test_one == '':
            msg = 'yes'
            return render(request, 'questions.html', {'msg': msg})
        else:
            sql_data = Questions.objects.create(title=test_one, detailDesc=test_two, lastModifiled=datetime.datetime.now(), answerCount=0)
            return redirect('/index/')
    return render(request, 'questions.html')


def Answer(request,id):
    # 使用get为啥会报错
    answer_one = Questions.objects.filter(id=id).first()
    if request.method == 'POST':
        answer_ss = request.POST.get('answer_num')
        if answer_ss != '':
            # 后面的qid_id = id 也可以写成qid = answer_one,这里我就有疑问了.为啥是等于一个对象
            sql_answer = Answers.objects.create(ansContent=answer_ss, ansDate=datetime.datetime.now(), qid_id=id)
        else:
            al = 'yes'
            return render(request, 'answer.html', {'al': al,
                                                   'id': id})

    answer_all = Answers.objects.filter(qid=id).all()
    return render(request, 'answer.html', {'answer_one': answer_one,
                                           'answer_all': answer_all,
                                           'id': id})

