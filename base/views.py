from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import  RequestForm
from .models import  Request
# Create your views here.



request_types = {
    '0':"New Creation",
    '1':"Option 1",
    '2':"Option 2"
}

def login(request):
    template = loader.get_template('base/login.html')


    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))



def request_form(request):
    template = loader.get_template('base/request_form.html')

    if request.method == 'POST':
        print("----------------------------")
        print(request.POST)
        print("----------------------------")

        username = request.POST.get('username')
        request_type = request_types[request.POST.get('request_type')]
        comment = request.POST.get('comment')
        attached_file = request.FILES.get('attached_file')

        form = Request.objects.create(
            username = username,
            request_type = request_type,
            comment = comment,
            attached_file=attached_file,

        )

        form.save()

        print("------------------------------------")

        return render(request, "base/login.html")
    else:
        form = RequestForm()

    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    requests = Request.objects.all()

    context = {
        "requests":requests
    }
    return render(request, "base/dashboard.html", context)

