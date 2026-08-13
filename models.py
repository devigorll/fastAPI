from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Cria conexão com o banco de dados SQLite
db = create_engine("sqlite:///banco.db")

# Cria a classe base para os modelos do SQLAlchemy
Base = declarative_base()

# Cria as classes / tabelas do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios_tb"

    id = Column( "id", Integer, primary_key = True, autoincrement = True)
    nome = Column("nome_usuario", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean)

    def __init__(self, nome_usuario, email, senha, ativo = True, admin = False):

        self.nome = nome_usuario
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos_tb"

    STATUS_PEDIDOS = (
        ("CANCELADO", "CANCELADO"),
        ("PENDENTE", "PENDENTE"),
        ("FINALIZADO", "FINALIZADO")
    )

    id = Column( "id", Integer, primary_key = True, autoincrement = True)
    status = Column("status", String(20)) 
    usuario = Column("usuario", ForeignKey("usuarios_tb.id"))
    preco = Column("preco", Float, nullable = False)
    # itens

    def __init__(self, usuario, status = "PENDENTE", preco = 0):
        self.usuario = usuario
        self.status = status
        self.preco = preco

class ItemPedido(Base):
    __tablename__ = "itens_pedido_tb"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    quantidade = Column("quantidade", Integer, nullable = False)
    sabor = Column("sabor", String(50), nullable = False)
    tamanho = Column("tamanho", String(20), nullable = False)
    preco_unitario = Column("preco_unitario", Float, nullable = False)
    pedido = Column("pedido", ForeignKey("pedidos_tb.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

# Executa a criação das tabelas no banco de dados
