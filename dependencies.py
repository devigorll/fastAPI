# ARQUIVO: dependencies.py

# OBJETIVO: 

# Este arquivo centraliza as funções de dependência (injções do FastAPI)
# utilizadas ao longo da aplicação. Sua principal função é gerenciar o 
# ciclo de vida das conexões com o banco de dados, garantindo que uma 
# sessão seja aberta quando uma requisição chega e obrigatoriamente 
# fechada após a resposta ser enviada.


# Importa o objeto de conexão/engine do banco de dados definido no arquivo models
from models import db

# Importa a fábrica de sessões do SQLAlchemy para criar conexões com o banco
from sqlalchemy.orm import sessionmaker


# Função geradora responsável por fornecer e gerenciar a sessão do banco de dados
def pegar_sessao():

    try:    
        # Configura a fábrica de sessões associando-a ao motor de banco de dados (db)
        Session = sessionmaker(bind=db)
        
        # Instancia uma nova sessão ativa de comunicação com o banco de dados
        session = Session()

        # O 'yield' faz com que a função pause e entregue a sessão para quem a solicitou.
        # A sessão permanece aberta e utilizável enquanto a rota/requisição estiver executando.
        yield session

    finally:
        # O bloco 'finally' SEMPRE é executado ao término da requisição (mesmo se ocorrer erro).
        # Garante o encerramento da conexão com o banco para não causar vazamento de conexões (connection leak).
        session.close()