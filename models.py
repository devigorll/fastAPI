# ARQUIVO: models.py

# OBJETIVO: 

# Este arquivo define a camada de dados (ORM) da aplicação utilizando SQLAlchemy.

# Nele são realizados:

# 1. A criação da conexão com o banco de dados (neste caso, SQLite).
# 2. A definição da classe Base que mapeia classes Python para tabelas relacionais.
# 3. A estrutura da tabela de Usuários (usuarios_tb), guardando credenciais e permissões.
# 4. A estrutura da tabela de Pedidos (pedidos_tb), com relacionamento de chave estrangeira para o usuário.
# 5. A estrutura da tabela de Itens do Pedido (itens_pedido_tb), com os detalhes de cada item e chave estrangeira para o pedido.


# Importação das ferramentas do SQLAlchemy para criação de tabelas, tipos de colunas e relacionamentos
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey

# Importação da classe base declarativa para mapeamento ORM das entidades
from sqlalchemy.orm import declarative_base

# Importação de tipo personalizado para lidar com escolhas pré-definidas (opções fixas)
from sqlalchemy_utils.types import ChoiceType


# Cria a conexão/engine com o banco de dados local SQLite (arquivo banco.db)
db = create_engine("sqlite:///banco.db")

# Cria a classe base da qual todos os modelos de tabelas do SQLAlchemy irão herdar
Base = declarative_base()


# Classe que mapeia a tabela de usuários no banco de dados
class Usuario(Base):
    # Nome definitivo da tabela no banco de dados
    __tablename__ = "usuarios_tb"

    # Mapeamento dos campos/colunas da tabela
    id = Column( "id", Integer, primary_key = True, autoincrement = True) # Chave primária autoincrementada
    nome = Column("nome_usuario", String)                                 # Nome do usuário
    email = Column("email", String)                                       # E-mail para identificação/login
    senha = Column("senha", String)                                       # Hash da senha criptografada
    ativo = Column("ativo", Boolean)                                     # Status se a conta está ativa ou inativa
    admin = Column("admin", Boolean)                                     # Define se o usuário tem privilégios de administrador

    # Método construtor para facilitar a criação de instâncias de Usuario com valores padrão
    def __init__(self, nome_usuario, email, senha, ativo = True, admin = False):
        self.nome = nome_usuario
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


# Classe que mapeia a tabela de pedidos no banco de dados
class Pedido(Base):
    # Nome definitivo da tabela no banco de dados
    __tablename__ = "pedidos_tb"

    # Tupla de opções com os status permitidos para controle do fluxo do pedido
    STATUS_PEDIDOS = (
        ("CANCELADO", "CANCELADO"),
        ("PENDENTE", "PENDENTE"),
        ("FINALIZADO", "FINALIZADO")
    )

    # Mapeamento dos campos/colunas da tabela
    id = Column( "id", Integer, primary_key = True, autoincrement = True)  # Chave primária do pedido
    status = Column("status", String(20))                                  # Estado atual do pedido (ex: PENDENTE)
    usuario = Column("usuario", ForeignKey("usuarios_tb.id"))               # Chave estrangeira ligando ao id do Usuario
    preco = Column("preco", Float, nullable = False)                       # Valor total do pedido (obrigatório)
    # itens

    # Método construtor com valores padrão para criar novos pedidos
    def __init__(self, usuario, status = "PENDENTE", preco = 0):
        self.usuario = usuario
        self.status = status
        self.preco = preco


# Classe que mapeia a tabela de itens que compõem um determinado pedido
class ItemPedido(Base):
    # Nome definitivo da tabela no banco de dados
    __tablename__ = "itens_pedido_tb"

    # Mapeamento dos campos/colunas da tabela
    id = Column("id", Integer, primary_key = True, autoincrement = True)  # Chave primária do item
    quantidade = Column("quantidade", Integer, nullable = False)          # Quantidade do produto (obrigatório)
    sabor = Column("sabor", String(50), nullable = False)                 # Sabor/nome do produto (obrigatório)
    tamanho = Column("tamanho", String(20), nullable = False)             # Tamanho (ex: Grande, Média) (obrigatório)
    preco_unitario = Column("preco_unitario", Float, nullable = False)    # Preço por unidade (obrigatório)
    pedido = Column("pedido", ForeignKey("pedidos_tb.id"))                # Chave estrangeira ligando ao id do Pedido

    # Método construtor para inicializar um item de pedido
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# Executa a criação das tabelas no banco de dados