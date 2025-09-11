# Django Careers API

API simples desenvolvida com Django e Django REST Framework para gerenciar posts de carreira. A API oferece funcionalidades completas de CRUD (Create, Read, Update, Delete) para posts, com **paginação** nas listas.

## Funcionalidades

- **Criar posts** - `POST /careers/`
- **Listar posts (com paginação)** - `GET /careers/`
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
    pip install -r requirements.txt
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

- **Listar todos os posts (com paginação)**
    ```bash
    curl http://127.0.0.1:8000/careers/
    ```
    **Parâmetros de paginação opcionais:**
    - `?page=2` → ir para a página 2
    - `?page_size=20` → definir quantos itens por página (se habilitado na configuração)

    **Exemplo de resposta:**
    ```json
    {
      "count": 35,
      "next": "http://127.0.0.1:8000/careers/?page=2",
      "previous": null,
      "results": [
        {"id": 1, "username": "joao", "title": "Meu título", "content": "Conteúdo"},
        {"id": 2, "username": "maria", "title": "Outro título", "content": "Mais conteúdo"}
      ]
    }
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
