from django.shortcuts import render
from django.views.generic import ListView
from typing import Any
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from aplic.models import Produto, Cliente


class CadastroLogin():
    def cadastro (request):
        if request.method == "GET":
            return render(request, "cadastro.html")
        else:
            nome = request.POST.get("nome")
            cpf = request.POST.get("cpf")

            user = Cliente.objects.filter(cpf=cpf).first()

            if user:
                return HttpResponse("Já existe usuario com esse cpf")
            
        
            user = Cliente.objects.create(nome=nome, cpf=cpf)
            user.save()

            return HttpResponse("Cadastrado")

    def login (request):
        if request.method == "GET":
            return render(request, "login.html")
        else:
            nome = request.POST.get("nome")
            cpf = request.POST.get("cpf")

            user = authenticate(nome=nome, cpf=cpf)

            if user:
                return HttpResponse("Logado")
            else:
                return HttpResponse("Email ou senha invalido")



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context

class DetalhesProdutoView(ListView):
    template_name = 'detalhe_produto.html'
    paginate_by = 5
    ordering = 'nome_produto'
    model = Produto

    def get_context_data(self, **kwargs: Any):
        context = super(DetalhesProdutoView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['produto'] = Produto.objects.filter(id=id).first
        return context

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")