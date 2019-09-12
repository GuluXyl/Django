from django.shortcuts import render
from message_form.models import Message

# Create your views here.
def message_form(request):
    if request.method == 'POST':
        # 取出页面上的数据放到数据库
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        message = request.POST.get('message','')

        message_num = Message()
        message_num.name = name
        message_num.email = email
        message_num.address = address
        message_num.message = message
        message_num.save()
        return render(request, 'message_form.html', {
            "message":message
        })
    # 取出数据库中的数据放到页面
    if request.method == 'GET':
        vars_all = {}
        all_messages = Message.objects.all()
        if all_messages:
            message_tab = all_messages[0]
            vars_all = {'message_tab':message_tab}
            return render(request,'message_form.html',vars_all)

