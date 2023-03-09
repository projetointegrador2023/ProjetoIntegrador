## Controle de estoque

### Como iniciar o projeto:

- Clone esse repositório
- Crie um ambiente virtual com Python 3 [instruções](https://cloud.google.com/python/docs/setup?hl=pt-br#linux)
- Instale as dependências (requirements.txt)
- Rode as migrações

Exemplo:
```sh
git clone https://github.com/projetointegrador2023/RepoProjetoIntegrador.git
cd CodigoFonte
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 romaneio_app/contrib/env_gen.py
python3 romaneio_app/manage.py migrate
python3 romaneio_app/manage.py createsuperuser
python3 romaneio_app/manage.py runserver
```