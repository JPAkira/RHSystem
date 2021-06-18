# RHSystem
<h3>Criar pasta do projeto</h3>

<h5>Criar a pasta onde você deseja que fique todos os arquivos do projeto</h5>

1. Criar Venv
    ```
    python -m venv venv
    ```

2. Ativar Venv
    ```
    .\venv\Scripts\Activate
    ```

<h3>Baixar o repositorio</h3>

colocar na pasta onde fica o projeto

3. Instalar os requirements.txt
    ```
    pip install -r requirements.txt
    ```
4. Configurar o banco de dados

5. setup/settings.py

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nome_do_banco',
            'USER': 'usuario_postgresql',
            'PASSWORD': 'senha',
            'HOST': 'localhost'
        }
    }
    ```

6. Criar os dados no banco
    ```
    python manage.py migrate
    ```
7. Iniciar o servidor</h3>
    ```
    python manage.py runserver
    ```
8. Executar teste
    ```
    python manage.py test
    ```
7. Para criar um usuário de empresa
Registre na área de empresa
8. Crie um superuser no django
    ```
    python manage.py createsuperuser
    ```
9. Logue no usuário superuser no painel django admin
www.linkapp/admin

10. Entre nos usuários e adicione permissão empresa para o usuário criado
