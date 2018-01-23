from django.contrib import messages
from django.shortcuts import render

from .forms import *


def index(request):
    template_name = 'panel/index.html'

    return render(request, template_name)


def funds(request):
    template_name = 'panel/add.html'

    form = FundForm(auto_id=False)

    title = 'Cadastro de fundo'

    if request.method == 'POST':
        form = FundForm(request.POST)

        if form.is_valid() is False:
            errors = form.errors.as_data()

            for error, val in errors.items():
                messages.error(request, ''.join(val[0]))  # Join the ValidationError value

        else:
            form.save()
            title = form.instance.name
            messages.success(request, 'Cadastrado com sucesso!')

    context = {
        'title': title,
        'form': form
    }

    return render(request, template_name, context)


def units(request):
    template_name = 'panel/add.html'

    form = UnitForm(auto_id=False)

    title = 'Cadastro de unidade'

    if request.method == 'POST':
        errors = form.errors.as_data()

        if form.is_valid is False:
            for error, val in errors.items():
                messages.error(request, ''.join(val[0]))  # Join the ValidationError value

        else:
            form.save()
            title = form.instance.name
            messages(request, 'Cadastrado com sucesso!')

    context = {
        'title': title,
        'form': form
    }

    return render(request, template_name, context)


def species(request):
    template_name = 'panel/add.html'

    form = SpecieForm(auto_id=False)

    title = 'Cadastro de espécie'

    if request.method == 'POST':
        errors = form.errors.as_data()

        if form.is_valid is False:
            for error, val in errors.items():
                messages.error(request, ''.join(val[0]))  # Join the ValidationError value

        else:
            form.save()
            title = form.instance.name
            messages(request, 'Cadastrado com sucesso!')

    context = {
        'title': title,
        'form': form
    }

    return render(request, template_name, context)


def logout(request):
    pass
