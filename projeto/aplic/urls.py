from django.urls import path
from .views import IndexView, MyView, DetalhesProdutoView, CadastroLogin

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("mine/", MyView.as_view(), name="my-view"),
    path("detalhes/<int:id>",DetalhesProdutoView.as_view(), name="detalhe_produto"),
    path("login/", CadastroLogin.login, name="login"),
    path("cadastro/", CadastroLogin.cadastro, name="cadastro")
]