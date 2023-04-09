## Dia 1

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
django-admin startproject nome_do_projeto
python3 manage.py startapp nome_da_app
```

### Links:
- [Python](https://www.python.org/downloads/)

## Dia 2

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
```bash
python3 mananage.py makemigrations
python3 manage.py migrate
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

## Dia 3

Verificar se o python está no path do windows e corretamente selecionado no VSCode

```bash
django-admin startproject mysite
```

- **manage.py**: Um utilitário de linha de comando que permite interagir com o projeto Django.

- **__init__.py**: Um arquivo vazio que diz ao Python que este diretório deve ser considerado um pacote Python.

- **settings.py**: Definições ou configuração do projeto.

```bash
python manage.py runserver
```

Para criar um app tenha certeza de estar no mesmo diretório do arquivo manage.py

```bash
python manage.py startapp core
```

Criando a primeira View:

#### core/views.py
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
```

Criando um arquivo urls.py no app para mapaear a view para uma url:

#### core/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Incluindo as nossa view customizada na raiz do nosso projeto:

#### romaneio/urls.py:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]
```

```bash
python manage.py runserver
```