# RHSystem
<h3>Criar pasta do projeto</h3>

<h5>Criar a pasta onde você deseja que fique todos os arquivos do projeto</h5>

<h3>Criar Venv</h3>
```sh
python -m venv venv
```

<h3>Ativar Venv</h3>

.\venv\Scripts\Activate

<h3>Baixar o repositorio</h3>

colocar na pasta onde fica o projeto

<h3>Instalar os requirements.txt</h3>

pip install -r requirements.txt

<h3>Configurar o banco de dados</h3>

setup/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario_postgresql',
        'PASSWORD': 'senha',
        'HOST': 'localhost'
    }
}

<h3>Criar os dados no banco</h3>

python manage.py migrate

<h3>Iniciar o servidor</h3>

python manage.py runserver

<h3>Executar teste</h3>

python manage.py test

