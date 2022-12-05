from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
# Create your views here.


def registr(reqeust):
    form = Registr_form()
    return render(reqeust, 'app/registr.html', {'form': form})


def weclom(reqeust):
    if reqeust.method == 'POST':
        form = Registr_form(reqeust.POST)
        if form.is_valid():
            return render(reqeust, 'app/welcome.html', {'data': [(i, form.cleaned_data[i]) for i in form.cleaned_data.keys()], 'text': f'{form.cleaned_data["Name"]} , поздравляю с регистрацией!'})
        else:
            form = Login(reqeust.POST)
            if form.is_valid():
                return render(reqeust, 'app/welcome.html', {'data': [(i, form.cleaned_data[i]) for i in form.cleaned_data.keys()], 'text': f'Поздравляю с успешным входом'})

            else:
                return HttpResponseRedirect('registr')
    else:
        return HttpResponseRedirect('registr')


def login(request):
    form = Login()
    return render(request, 'app/login.html', {'form': form})