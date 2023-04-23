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
Criando a primeira View

`app_hello/views.py`
```python
from django.http import HttpResponse

def function_hello(request):
    return HttpResponse("Hello World")
```

Criando um arquivo urls.py no app hello para mapaear a view para uma url

`app_hello/urls.py`
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.function_hello),
]
```
Incluindo o path (url) da nossa view customizada na raiz do nosso projeto

Se for uma função:

`projeto/urls.py`

1. Import a view correspondente:
```python
from app_hello import views
```	 
2. Adicione a URL ao conjunto de URLs do projeto:
```python
path('hello/', views.funcao_hello)
```
Se for uma classe:

`projeto/urls.py`

1. Importe a classe:
```python
	from app_hello.views import Classe
```
2. Adicione a URL ao conjunto de URLs do projeto (projeto/urls.py):
```python
path('Classe/', Classe.as_view())
```
Rode o servidor
```bash
python manage.py runserver
```

## Dia 4 (Templates)

Criar um novo app chamado **app_index**
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

Criando a view do app index

`app_index/views.py`

```python
from django.shortcuts import render

def funcao_index(request):
    return render(request, 'index.html')
```

Criando um arquivo urls.py no app para mapaear a view para uma url

`app_index/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
	path('index/', views.funcao_index),
]
```

Incluindo o path da view na raiz do projeto

`projeto/urls.py:`
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('app_hello.urls')),
	path('', include('app_index.urls')), # incluindo path do app index	
]
```
Criando um arquivo index.html e adicionando uma simples tag html para testar se funcionou

`app_index/templates/index.html`
```html
<h1>INDEX</h1>
```

Por fim adicione o diretório do template no arquivo `settings.py` do projeto
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
      # 'DIRS': [],
        'DIRS': [
            os.path.join(BASE_DIR, 'app_index', 'templates')
            ],
        'APP_DIRS': True,
    }
]
```
Rode o servidor
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

Extendendo as configurações do arquivo base.html para o arquivo **index.html**

`index.html`
```html
{% extends 'base.html' %}

{% block title %}Página Index{% endblock %}

{% block content %}

<h1>INDEX</h1>

{% end block %}
```
Rode o servidor
```bash
python manage.py runserver
```

## Dia 5 (Models)

Criar um aplicativo chamado **notas_fiscais**
```
python manage.py startapp notas_fiscais
```

No arquivo `notas_fiscais/models.py`, criar um modelo para a nota fiscal
```python
from django.db import models

class NotaFiscal(models.Model):
    numero = models.IntegerField()
    data_emissao = models.DateField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
```

Criar uma view para a nota fiscal no arquivo `notas_fiscais/views.py`
```python
from django.shortcuts import render
from .models import NotaFiscal

def nota_fiscal(request, nota_fiscal_id):
    nota_fiscal = NotaFiscal.objects.get(pk=nota_fiscal_id)
    return render(request, 'nota_fiscal.html', {'nota_fiscal': nota_fiscal})
```

Criar um template HTML para a nota fiscal em `notas_fiscais/templates/nota_fiscal.html`
```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>Minha nota fiscal</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/nota_fiscal.css' %}">
    <script type="text/javascript" src="{% static 'js/nota_fiscal.js' %}"></script>
</head>
<body>
    <form>
        <label for="numero">Número:</label>
        <input type="number" id="numero" name="numero"><br>

        <label for="data_emissao">Data de emissão:</label>
        <input type="date" id="data_emissao" name="data_emissao"><br>

        <label for="valor_total">Valor total:</label>
        <input type="number" step="0.01" id="valor_total" name="valor_total"><br>

        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

Criar o arquivo CSS em `notas_fiscais/static/css/nota_fiscal.css`

```css
/* Define a fonte e tamanho padrão */
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 14px;
}

/* Estilo para o título da página */
h1 {
  font-size: 28px;
  text-align: center;
  margin-top: 30px;
  margin-bottom: 30px;
}

/* Estilo para o formulário */
form {
  width: 60%;
  margin: 0 auto;
}

/* Estilo para o rótulo do campo de entrada */
label {
  display: block;
  margin-top: 20px;
}

/* Estilo para o campo de entrada */
input[type="text"],
input[type="number"],
input[type="date"] {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 5px;
  margin-bottom: 10px;
}

/* Estilo para o botão de envio */
input[type="submit"] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

/* Estilo para as mensagens de erro */
.error-message {
  color: red;
  margin-top: 5px;
}

/* Estilo para a mensagem de sucesso */
.success-message {
  color: green;
  margin-top: 5px;
}
```


Criar o arquivo JavaScript em `notasfiscais/static/js/nota_fiscal.js`

```js
const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    // Obtém os valores dos campos do formulário
    const numero = document.querySelector('#numero').value;
    const data_emissao = document.querySelector('#data_emissao').value;
    const valor_total = document.querySelector('#valor_total').value;

    // Valida os campos do formulário
    const errors = [];
    if (!numero) {
        errors.push('O número da nota fiscal é obrigatório.');
    }
    if (!data_emissao) {
        errors.push('A data de emissão é obrigatória.');
    }
    if (!valor_total) {
        errors.push('O valor total é obrigatório.');
    }

    if (errors.length > 0) {
        // Se houver erros, exibe-os na tela
        const errorElement = document.querySelector('#form-errors');
        errorElement.innerHTML = '';
        errors.forEach((error) => {
            const li = document.createElement('li');
            li.textContent = error;
            errorElement.appendChild(li);
        });
    } else {
        // Se não houver erros, envia os dados do formulário para o servidor
        const nota_fiscal = {
            numero: numero,
            data_emissao: data_emissao,
            valor_total: valor_total,
        };

        fetch('/notas_fiscais/criar_nota_fiscal/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(nota_fiscal),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Nota fiscal criada com sucesso:', data);
            // Redireciona o usuário para a página da nota fiscal criada
            window.location.href = '/notas_fiscais/' + data.id + '/';
        })
        .catch(error => {
            console.error('Erro ao criar nota fiscal:', error);
        });
    }
});
```

Adicionar o aplicativo `notasfiscais` e o diretório `templates` ao arquivo `settings.py` do projeto
```python
INSTALLED_APPS = [
    ...
    'notasfiscais',
    ...
]

TEMPLATES = [
    {
        ...
        'APP_DIRS': True,
        ...
    },
]
```

Criar uma URL para a view da nota fiscal em `notas_fiscais/urls.py`
```md
O <int:nota_fiscal_id> é uma expressão regular que define uma parte variável do caminho da URL, 
que deve ser um número inteiro. Essa parte variável é capturada e passada para a função nota_fiscal 
como um argumento com o nome nota_fiscal_id.
```

```python
from django.urls import path
from . import views

urlpatterns = [
    path('nota_fiscal/<int:nota_fiscal_id>/', views.nota_fiscal, name='nota_fiscal'),
]
```

Inclua as URLs do aplicativo no arquivo `urls.py` do projeto
```python
from django.urls import include, path

urlpatterns = [
    path('', include('notasfiscais.urls')),
]
```

Rode o servidor
```
python manage.py runserver
```
Para acessar uma nota fiscal específica, você precisa acessar `http://localhost:8000/nota_fiscal/1/` - *substitua "1" pelo ID da nota fiscal desejada*