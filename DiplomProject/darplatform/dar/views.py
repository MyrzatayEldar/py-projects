from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from dar.models import *
from .forms import *
from .utils import *
from django.template import RequestContext


def load_main(request):
    data = JaiModel.objects.all()
    x = [x.name for x in data]
    y = [y.how_many for y in data]
    chart = get_plot(x, y)
    context = {
        'chart': chart
    }
    return render(request, 'dar/main.html', context=context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            same_data_exists = ProfileLoginAndPassword.objects.filter(login=request.POST['login'],
                                                                      password=request.POST['password'])
            print(same_data_exists)
            if same_data_exists:
                return redirect('main')

            else:
                return HttpResponse('<h1>User like this doesnt exist.</h1>')
    else:
        form = LoginForm()
    return render(request, 'dar/login.html', context={'form': form})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance = ProfileInfo(**form.cleaned_data)
            username, password = gen_login_and_pass(form.cleaned_data['first_name'], form.cleaned_data['surname'])
            instance1 = ProfileLoginAndPassword(login=username, password=password)
            message = str(username) + '\n' + str(password)
            print(send_success_mess(who=form.cleaned_data['email'],
                                    message=message))
            instance.save()
            instance1.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'dar/registration.html', context={'form': form})
