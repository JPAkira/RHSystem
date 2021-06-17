# RHSystem
 
#Criar pasta do projeto 

Criar a pasta onde você deseja que fique todos os arquivos do projeto

#Criar Venv

python -m venv venv

#Ativar Venv

.\venv\Scripts\Activate

#Baixar o repositorio

colocar na pasta onde fica o projeto

#Instalar os requirements.txt

pip install -r requirements.txt

#Configurar o banco de dados

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

#Criar os dados no banco

python manage.py migrate

#Iniciar o servidor

python manage.py runserver

#Executar teste

python manage.py test

