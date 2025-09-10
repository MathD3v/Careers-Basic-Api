# Django Careers API

API simples desenvolvida com Django e Django REST Framework para gerenciar posts de carreira. A API oferece funcionalidades completas de CRUD (Create, Read, Update, Delete) para posts.

## Funcionalidades

- **Criar posts** - `POST /careers/`
- **Listar posts** - `GET /careers/`
- **Atualizar posts** - `PATCH /careers/{id}/`
- **Deletar posts** - `DELETE /careers/{id}/`

## Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- Git (opcional, para clonar o repositório)

## Instalação

1. **Clone o repositório**
    ```bash
    git clone https://github.com/MathD3v/CodeLeep.git
    cd backend
    ```

2. **Crie um ambiente virtual**

    - Linux/macOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - Windows (CMD):
      ```cmd
      python -m venv venv
      venv\Scripts\activate
      ```
    - Windows (PowerShell):
      ```powershell
      python -m venv venv
      venv\Scripts\Activate.ps1
      ```

3. **Instale as dependências**
    ```bash
    pip install django djangorestframework django-cors-headers
    ```

4. **Configure o banco de dados**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Execute o servidor**
    ```bash
    python manage.py runserver
    ```
    O servidor estará disponível em: `http://127.0.0.1:8000`

## Endpoints da API

- **Criar um post**
    ```bash
    curl -X POST http://127.0.0.1:8000/careers/ \
      -H "Content-Type: application/json" \
      -d '{"username":"joao","title":"Meu título","content":"Conteúdo"}'
    ```

- **Listar todos os posts**
    ```bash
    curl http://127.0.0.1:8000/careers/
    ```

- **Atualizar um post específico**
    ```bash
    curl -X PATCH http://127.0.0.1:8000/careers/1/ \
      -H "Content-Type: application/json" \
      -d '{"title":"Novo título","content":"Novo conteúdo"}'
    ```

- **Deletar um post**
    ```bash
    curl -X DELETE http://127.0.0.1:8000/careers/1/
    ```

## Tecnologias Utilizadas

- **Django** - Framework web Python  
- **Django REST Framework** - Toolkit para construção de APIs REST  
- **Django CORS Headers** - Gerenciamento de CORS  

## Configurações Importantes

### CORS

Durante o desenvolvimento, o CORS está configurado para aceitar todas as origens:

```python
CORS_ALLOW_ALL_ORIGINS = True

## Limitações Atuais

- Sem sistema de autenticação
- Sem controle de acesso/permissões
- Sem validações avançadas
- Sem paginação