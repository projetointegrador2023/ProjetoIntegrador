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

`app_index/templates/base.html`
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

Criar um app chamado nota_fiscal:
```sh
python manage.py startapp nota_fiscal
```
Abrir o arquivo `models.py` dentro do diretório `nota_fiscal` e defina o modelo da nota fiscal
```py
from django.db import models

class NotaFiscal(models.Model):
    data_emissao = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
```
Abra o arquivo `admin.py` dentro do diretório `nota_fiscal` e registre o modelo
```py
from django.contrib import admin
from .models import NotaFiscal

admin.site.register(NotaFiscal)
```
Criar a views para a criação de notas fiscais no arquivo `views.py` dentro do diretório `nota_fiscal`
```py
from django.shortcuts import render
from .forms import NotaFiscalForm

def criar_nota_fiscal(request):
    if request.method == 'POST':
        form = NotaFiscalForm(request.POST)
        if form.is_valid():
            form.save()                       
    else:
        form = NotaFiscalForm()
    return render(request, 'criar_nota_fiscal.html', {'form': form})
```
Crie um formulário para criação de notas fiscais no arquivo `forms.py` dentro do diretório `nota_fiscal`
```py
from django import forms
from .models import NotaFiscal

class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = ['data_emissao', 'valor_total']
```
Configure as rotas para as views no arquivo `urls.py` dentro do diretório `nota_fiscal`
```py
from django.urls import path
from . import views

urlpatterns = [    
    path('create/', views.nota_fiscal_create, name='nota_fiscal_create'),
]
```
Configure as rotas do app no arquivo `urls.py` dentro do diretório `projeto`
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nota_fiscal/', include('nota_fiscal.urls')),
]
```
Crie o template `criar_nota_fiscal.html` em `nota_fiscal/templates/nota_fiscal/` com o seguinte código

```html
<!DOCTYPE html>
<html lang="en">
<head>
<head>
    <meta charset="UTF-8">
    <title>Nota Fiscal</title>
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'notafiscal/css/style.css' %}">
    <script type="text/javascript" src="{% static 'notafiscal/js/script.js' %}"></script>
</head>

</head>
<body>
  <header>
    <h1>Nota Fiscal</h1>
  </header>

  <main>
    <form method="post">
      {% csrf_token %}
      <div>
        <label for="data_emissao">Data de Emissão:</label>
        <input type="date" id="data_emissao" name="data_emissao" required>
      </div>
      <div>
        <label for="valor_total">Valor Total:</label>
        <input type="number" id="valor_total" name="valor_total" step="0.01" required>
      </div>
      <button type="submit">Enviar</button>
    </form>

    {% if notas_fiscais %}
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Data de Emissão</th>
            <th>Valor Total</th>
          </tr>
        </thead>
        <tbody>
          {% for nf in notas_fiscais %}
            <tr>
              <td>{{ nf.id }}</td>
              <td>{{ nf.data_emissao|date:"d/m/Y" }}</td>
              <td>{{ nf.valor_total }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p>Não há notas fiscais registradas.</p>
    {% endif %}
  </main>

  <script src="{% static 'js/criar.js' %}"></script>
</body>
</html>
```

Crie uma pasta chamada `static` no diretório do app `nota_fiscal` se ela ainda não existir. Dentro dela, crie duas pastas: `css` e `js`.
Dentro da pasta `css`, crie um arquivo chamado `criar.css`. E dentro da pasta `js`, crie um arquivo chamado `criar.js`.

O arquivo `criar.css` terá o seguinte conteúdo:
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f2f2f2;
}

header {
  background-color: #333;
  color: white;
  padding: 20px;
}

h1 {
  font-size: 2em;
}

main {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
}

input {
  padding: 5px;
  border: none;
  border-radius: 5px;
}

button {
  margin-top: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #333;
  color: white;
  cursor: pointer;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 10px;
  text-align: center;
  border: 1px solid #ddd;
}

thead {
  background-color: #333;
  color: white;
}

tbody tr:nth-child(even) {
  background-color: #f2f2f2;
}

p {
  margin-top: 20px;
  text-align: center;
  font-style: italic;
  color: #999;
}
```

O arquivo `criar.js` terá o seguinte conteúdo:

```js
// Para exibir mensagem de confirmação após o envio do formulário
const form = document.querySelector('form');
form.addEventListener('submit', function(e) {
  const confirmacao = confirm('Deseja realmente enviar essa nota fiscal?');
  if (!confirmacao) {
    e.preventDefault();
  }
});
```

Adicione a URL da view registrar_nota_fiscal ao arquivo urls.py do app nota_fiscal:
```py
from django.urls import path
from .views import listar_notas_fiscais, registrar_nota_fiscal

urlpatterns = [
    path('criar/', registrar_nota_fiscal, name='nota_fiscal_criar'),
]
```
Depois disso, rode as migrações para criar o novo banco de dados do SQLite
```sh
python manage.py makemigrations
python manage.py migrate
``` 
Agora, quando o usuário acessar a URL `/nota_fiscal/criar/`, ele verá o formulário para criar uma nova nota fiscal.
Ao enviar o formulário, uma nova instância de NotaFiscal será criada e salva no banco de dados.
```sh
python manage.py runserver
```
