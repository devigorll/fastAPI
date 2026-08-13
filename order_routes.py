# ARQUIVO: order_routes.py

# OBJETIVO: 

# Este arquivo é responsável por gerenciar as rotas relacionadas aos pedidos da aplicação.
# Nele são definidas as rotas HTTP de acesso a esse módulo, tais como:
# 1. Rota raiz/boas-vindas da seção de pedidos.
# 2. Rota POST para a criação de novos pedidos vinculados a um usuário específico.


# Importações do FastAPI para criação de roteadores, injeção de dependências e tratamento de exceções HTTP
from fastapi import APIRouter, Depends, HTTPException, status

# Importação do modelo Pedido (tabela do banco de dados) e do motor do banco db
from models import Pedido, db

# Ferramenta do SQLAlchemy para gerenciamento e criação de sessões
from sqlalchemy.orm import sessionmaker

# Importação da função gerenciadora do ciclo de vida da sessão do banco de dados
from dependencies import pegar_sessao

# Importação do contexto de criptografia (Bcrypt) do arquivo principal
from main import bcrypt_context

# Importação do Schema Pydantic para validação e estruturação dos dados recebidos na criação do pedido
from schemas import PedidoSchema

# Tipo estático para anotação de tipos da sessão do SQLAlchemy
from sqlalchemy.orm import Session 


# Criação do roteador do FastAPI específico para ordens/pedidos
# prefix="/order": todas as rotas neste arquivo iniciam com o caminho /order
# tags=["order"]: agrupa as rotas sob a aba "order" na documentação interativa (Swagger)
order_router = APIRouter(prefix = "/order", tags = ["order"])


# Rota HTTP GET no caminho raiz de pedidos (/order/)
@order_router.get("/")
async def pedidos():

    '''
        Essa é a rota padrão de pedidos do nosso sistema.
    '''

    # Retorna uma mensagem de confirmação em formato JSON
    return {"mensagem": "Você acessou a rota de pedidos"}


# Rota HTTP POST para registro e criação de um novo pedido (/order/pedido)
@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    # Instancia um novo objeto Pedido utilizando o ID do usuário enviado pelo schema da requisição
    novo_pedido = Pedido(usuario = pedido_schema.usuario)

    # Adiciona a nova instância do pedido à fila da sessão ativa do banco
    session.add(novo_pedido)
    
    # Executa a gravação definitiva da transação no banco de dados
    session.commit()

    # Retorna a mensagem de confirmação de cadastro do pedido em formato JSON
    return {"mensagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.usuario}"}