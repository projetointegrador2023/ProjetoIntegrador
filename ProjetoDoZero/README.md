**Dia 1**

Instalação:
- Python
- Pip
- Django

Comandos:
```bash
- python --version ou python -V
- pip --version
- python -m pip install --upgrade pip
- pip install django
- django-admin startproject nome_do_projeto
- python3 manage.py startapp nome_da_app
```

Links:
- [Python](https://www.python.org/downloads/)

**Dia 2**

Instalação:
- OpenSSH Client
- Git

Comandos:
```bash
- Get-Service ssh-agent | Set-Service -StartupType Automatic -PassThru | Start-Service # PowerShell
- eval "$(ssh-agent -s)"
- ssh-keygen -t rsa -f ~/.ssh/nome_da_chave
- ssh-add ~/.ssh/nome_da_chave
- touch  ~/.ssh/config
- clip < ~/.ssh/id_ed25519.pub
- git config --global user.name "nome_do_usuario"
- git config --global user.email "email_do_usuario"
- git remote set-url origin "git@github.com:username/repository.git"
- git clone link_do_repositorio
- git status
- git commit -m "comentario"
- git push
- python3 mananage.py makemigrations
- python3 manage.py migrate
```
Mudar credenciais do Git no Windows (caso use mais de uma conta no GitHub):
> Painel de Controle > Gerenciador de Credenciais > Credenciais do Windows > Credenciais Genéricas (remove as credenciais do Git para fazer autenticação novamente)

Links:
- [Git](https://git-scm.com/downloads)