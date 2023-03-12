## WebApp de Romaneio

### Como iniciar o projeto:

- Clone esse repositório
- Crie um ambiente virtual - **[instruções](https://cloud.google.com/python/docs/setup?hl=pt-br#linux)**
- Instale as dependências - **requirements.txt**
- Rode as migrações

Exemplo:
```bash
git clone https://github.com/projetointegrador2023/ProjetoIntegrador.git
cd CodigoFonte
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cd romaneio_app
python3 contrib/env_gen.py
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```