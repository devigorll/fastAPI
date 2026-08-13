 # 🍕 Sistema de Delivery - API REST com FastAPI & Python
 
 Este repositório contém a implementação do backend completo para um **Sistema de Delivery (Pizzaria)** desenvolvido em Python utilizando **FastAPI**. 
 
 O projeto foi construído acompanhando a playlist/curso **[Curso de FastAPI - REST API com Python (Backend Completo)](https://www.youtube.com/playlist?list=PLpdAy0tYrnKy3TvpCT-x7kGqMQ5grk1Xq)** ministrado pelo canal **Hashtag Programação**.
 
 ---

 > Projeto em desenvolvimento
 
 ## 📌 Objetivo do Projeto & Estudos
 
 O objetivo principal deste projeto é servir como objeto de estudo prático para dominar a criação de Web APIs modernas, performáticas e assíncronas com Python.
 
 **Competências desenvolvidas:**
 - Entendimento arquitetural de uma aplicação **REST API**.
 - Desenvolvimento de rotas assíncronas (`async/await`) focadas em alta performance.
 - Modelagem e persistência de dados com **SQLAlchemy ORM**.
 - Validação e serialização de dados de entrada/saída utilizando o **Pydantic**.
 - Implementação de autenticação e segurança via **OAuth2**, **JWT (JSON Web Tokens)** e **Bcrypt**.
 - Capacidade de estruturar backends completos para integrar com aplicações front-end/mobile ou consumir APIs de terceiros.
 
 ---
 
 ## 🛠️ Tecnologias Utilizadas
 
 - **[Python 3](https://www.python.org/)**
 - **[FastAPI](https://fastapi.tiangolo.com/)**: Framework moderno e de alta performance para construção de APIs.
 - **[Uvicorn](https://www.uvicorn.org/)**: Servidor web ASGI rápido. 
 - **[SQLAlchemy](https://www.sqlalchemy.org/)**: ORM para manipulação e integração com banco de dados.
 - **[Pydantic](https://docs.pydantic.dev/)**: Validação e parsing de dados com tipagem estática.
 - **[PassLib / Bcrypt](https://passlib.readthedocs.io/)**: Hashing seguro e criptografia de senhas.
 - **[Python-Jose](https://python-jose.readthedocs.io/)**: Criação, validação e manipulação de tokens JWT.
 - **[SQLite](https://www.sqlite.org/)**: Banco de dados relacional (ambiente de desenvolvimento).
 
 ---
 
 ## 📂 Estrutura da Aplicação
 
 A arquitetura do projeto foi dividida em módulos responsáveis por papéis específicos na aplicação:
 
 - **`main.py`**: Ponto de entrada da aplicação FastAPI, inicialização do servidor e inclusão dos roteadores.
 - **`models.py`**: Definição das tabelas e entidades do banco de dados (`Usuario`, `Pedido`, `ItemPedido`) utilizando o SQLAlchemy.
 - **`schemas.py`**: Schemas e modelos do Pydantic para validação das requisições e respostas da API.
 - **`dependencies.py`**: Gerenciador de ciclo de vida do banco de dados (gerenciamento e encerramento de conexões por requisição).
 - **`auth_routes.py`**: Rotas dedicadas ao fluxo de usuários (Cadastro, Login e Autenticação).
 - **`order_routes.py`**: Rotas para controle, criação e listagem de pedidos e itens do sistema de delivery.
 
 ---
 
 ## 🚀 Como Executar o Projeto
 
 ### Pré-requisitos
 - Python 3.10+ instalado.
 - Git instalado.
 
 ### Passo a Passo
 
 1. **Clonar o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```
 
 2. **Criar e ativar o Ambiente Virtual (venv):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
 
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```
 
 3. **Instalar as dependências:**
    ```bash
    pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv
    ```
 
 4. **Executar a aplicação:**
    ```bash
    uvicorn main:app --reload
    ```
 
 5. **Acessar a documentação interativa:**
    Acesse o seu navegador em:
    - **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
 
 ---
 
 ## 👨‍💻 Autor
 
 Desenvolvido por **Igor Cruz** como parte do plano de estudos em Ciência de Dados e Desenvolvimento Backend Python.
 
 - **LinkedIn:** [Seu Link do LinkedIn]
 - **GitHub:** [Seu Link do GitHub]
 
 ---
 
 ## 🙏 Agradecimentos
 
 Projeto construído com base nas aulas gratuitas disponibilizadas pelo canal **Hashtag Programação** na playlist [Curso de FastAPI - Rest API com Python](https://www.youtube.com/playlist?list=PLpdAy0tYrnKy3TvpCT-x7kGqMQ5grk1Xq).