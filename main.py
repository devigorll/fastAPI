# ARQUIVO: main.py

# OBJETIVO: 

# Este arquivo é o ponto de entrada principal da aplicação FastAPI.
# Ele é responsável por:
# 1. Carregar configurações globais e variáveis de ambiente (como SECRET_KEY).
# 2. Inicializar a instância principal da aplicação web FastAPI.
# 3. Configurar instâncias globais de segurança e criptografia (Bcrypt).
# 4. Registrar e unificar todas as rotas/módulos do sistema (como auth e orders).


# Importa a classe principal do framework FastAPI para instanciar a aplicação
from fastapi import FastAPI

# Importa o gerenciador de contextos de criptografia da biblioteca PassLib (usado para senhas)
from passlib.context import CryptContext

# Importa a função para carregar variáveis de ambiente a partir de um arquivo .env
from dotenv import load_dotenv

# Módulo nativo do Python para interagir com o sistema operacional e ler variáveis de ambiente
import os


# Carrega as variáveis de ambiente personalizadas declaradas no arquivo .env para a memória
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Lê o valor da variável de ambiente 'SECRET_KEY' (usada para assinar tokens e dados sensíveis)
SECRET_KEY = os.getenv("SECRET_KEY")  # Obt


# Cria a instância principal da aplicação FastAPI (utilizada pelo servidor Uvicorn para rodar o projeto)
app = FastAPI() # uvicorn main:app --reload 


# Configura o algoritmo de criptografia de senhas (define o Bcrypt como padrão e lida com algoritmos legados)
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Importa os roteadores de rotas específicos de cada módulo da aplicação
from auth_routes import auth_router
from order_routes import order_router


# Inclui e conecta os roteadores na aplicação principal
# Registra as rotas de autenticação (/auth) no app
app.include_router(auth_router)

# Registra as rotas de pedidos/ordens no app
app.include_router(order_router)