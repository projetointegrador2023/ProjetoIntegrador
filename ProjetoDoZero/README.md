## Dia 1 (Instalação do Python e do Django)

### Configuração:
- Python
- Pip
- Django

### Comandos:
Execute o CMD ou Prompt de Comando como administrador
```bash
python --version ou python -V
pip --version
python -m pip install --upgrade pip
pip install django
```
Abra um terminal no seu VSCode ou Pycharm
```bash
django-admin startproject teste_projeto
python3 manage.py startapp teste_app
```

### Links:
- [Python](https://www.python.org/downloads/)

## Dia 2 (Git e GitHub)

### Configuração:
- OpenSSH Client
- Git

Habilite o OpenSSH Client no Windows:

> Pesquisar > Gerenciar Recursos Opcionais

Execute o seguinte comando no PowerShell (como administrador) depois de habilitar o OpenSSH Client:
```bash
Get-Service ssh-agent | Set-Service -StartupType Automatic -PassThru | Start-Service #Habilita o ssh-agent para iniciar automaticamente
```
Reinicie o computador.

### Comandos:
Execute esses comandos no Git Bash (botão direito), dentro da pasta que você quer clonar o repositório:
```bash
git config --global user.name "nome_do_usuario"
git config --global user.email "email_do_usuario"
git clone "git@github.com:username/repository.git
git remote set-url origin "git@github.com:username/repository.git"
```
```bash
eval "$(ssh-agent -s)" # Habilita o agent para o shell atual
ssh-keygen -t rsa -f ~/.ssh/nome_da_chave # Gera uma chave ssh
ssh-add ~/.ssh/nome_da_chave # Adiciona a chave ssh ao agent
clip < ~/.ssh/nome_da_chave.pub # Copia a chave ssh - certifique-se de escolher a chave que termina com .pub
```
Vá até o repositório do GitHub e adicione a chave que você copiou:

> github.com > settings > SSH and GPG Keys > New SSH Key

Abra um terminal no seu VSCode ou Pycharm:
```bash
git status
git commit -m "comentario"
git push
```

### Configurar mais de uma chave SSH no Windows:

Crie um arquivo chamado **config** no diretório abaixo:

> C:\Users\nome_do_usuario\\.ssh

Caso não encontre a pasta .ssh, coloque para exibir itens ocultos ou crie uma.

Coloque o texto abaixo no arquivo **config** que você acabou de criar, e substitua o nome da chave pelo nome que você usou para criar a sua:
```sh
Host github.com-ProjetoIntegrador
	HostName github.com
	User git
	IdentityFile ~/.ssh/projeto_key

Host github.com-Pessoal
	HostName github.com
	User git
	IdentityFile ~/.ssh/windows_key
```

Entre no Painel de controle e procure pelo Gerenciador de credenciais:

> Painel de Controle > Gerenciador de Credenciais > Credenciais do Windows > Credenciais Genéricas

Remova as credenciais do Git para fazer autenticação novamente.

### Links:
- [Git](https://git-scm.com/downloads)

## Dia 3 (Views e Urls)

Verificar se o python está no path do windows e corretamente selecionado no VSCode

```bash
django-admin startproject projeto
```

- **manage.py**: Um utilitário de linha de comando que permite interagir com o projeto Django.

- **__init__.py**: Um arquivo vazio que diz ao Python que este diretório deve ser considerado um pacote Python.

- **settings.py**: Definições ou configuração do projeto.

Testar se o servidor está executando corretamente:
```bash
python manage.py runserver
```

Para criar um app tenha certeza de estar no mesmo diretório do arquivo **manage.py**
```bash
python manage.py startapp app_hello
```

Registrando o novo app no arquivo **settings.py**
```py
INSTALLED_APPS = [
	'app_hello',
]
```
Criando a primeira View:

#### app_hello/views.py
```python
from django.http import HttpResponse

def function_hello(request):
    return HttpResponse("Hello World")
```

Criando um arquivo urls.py no app hello para mapaear a view para uma url:

#### app_hello/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.function_hello),
]
```

Incluindo o path(url) da nossa view customizada na raiz do nosso projeto:

#### projeto/urls.py:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hello/', include('app_hello.urls')), # path do app hello
	path('admin/', admin.site.urls),
]
```

```bash
python manage.py runserver
```

## Dia 4 (Templates)
```sh
python manage.py startapp app_index
```

Registrando o novo app no arquivo **settings.py**
```py
INSTALLED_APPS = [
	'app_index',
]
```
É necessário criar uma pasta chamada **templates** dentro da pasta do app index, pois é lá que o Django vai buscar o arquivo index.html que será criado, bem como outros arquivos estáticos.

Criando a View do app index:

#### app_index/views.py
```python
from django.http import HttpResponse

def function_index(request):
    return render(request, 'index.html')
```

Criando um arquivo urls.py no app para mapaear a view para uma url:

#### app_index/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.function_index),
]
```

Incluindo o path da view na raiz do projeto:

#### projeto/urls.py:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('hello/', include('app_hello.urls')),
	path('index/', include('app_index.urls')), # path do app index
	path('admin/', admin.site.urls),
]
```
Criando um arquivo index.html e adicionando uma simples tag html para testar se funcionou:

#### app_index/templates/index.html
```html
<h1>INDEX</h1>
```

```bash
python manage.py runserver
```

Criar o arquivo **base.html** na pasta *templates* do app index, para usar as extensões de templates (templates tags):

#### app_index/templates/base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
	<pre>
		Conteúdo de exemplo do arquivo base.html,
		que será extendido para qualquer outro arquivo html
		que usar a template tag {% extends 'base.html' %}
	</pre>
	{% block content %}
	{% endblock %}    
</body>
</html>
```

Extendendo as configurações do arquivo base.html para o arquivo **index.html**:

#### index.html
```html
{% extends 'base.html' %}

{% block title %}Página Index{% endblock %}

{% block content %}

<h1>INDEX</h1>

{% end block %}
```

```bash
python manage.py runserver
```