# ARQUIVO: auth_routes.py

# OBJETIVO: 

# Este arquivo é responsável por gerenciar toda a camada de autenticação
# da aplicação. Nele são definidas as rotas HTTP de acesso público e 
# protegido relacionadas a usuários, como:

# 1. Teste de conexão/boas-vindas da rota de autenticação.
# 2. Criação de novas contas de usuário (cadastro com hash de senha).
# 3. Autenticação e login (validação de credenciais e geração de token).


# Importações do FastAPI para criação de rotas, injeção de dependências e manipulação de erros HTTP
from fastapi import APIRouter, Depends, HTTPException, status

# Importação dos modelos de banco de dados (Tabela Usuario e instância do DB)
from models import Usuario, db

# Ferramenta do SQLAlchemy para gerenciar a sessão de comunicação com o banco de dados
from sqlalchemy.orm import sessionmaker

# Importação da função de dependência que fornece a sessão ativa do banco de dados
from dependencies import pegar_sessao

# Importação do contexto de criptografia (Bcrypt) vindo do arquivo principal
from main import bcrypt_context

# Importação dos Schemas (Pydantic) para validação e estruturação dos dados recebidos nas requisições
from schemas import UsuariosSchema, LoginSchema

# Tipo estático para tipagem da sessão do SQLAlchemy nas funções
from sqlalchemy.orm import Session 


# Criação do roteador do FastAPI específico para autenticação
# prefix="/auth": todas as rotas deste arquivo começarão com /auth (ex: /auth/login)
# tags=["auth"]: agrupa essas rotas sob a categoria "auth" na documentação automática (Swagger)
auth_router = APIRouter(prefix = "/auth", tags = ["auth"])


# Função auxiliar temporária/fictícia para simular a geração de um token de acesso (JWT)
def criar_token(id_usuario):
    # Gera uma string simulando o token concatenado com o ID do usuário
    token = f"dksjkdjg{id_usuario}"
    return token


# Rota HTTP GET no caminho raiz da autenticação (/auth/)
@auth_router.get("/")
async def home():
    '''
        Essa é a rota padrão de autenticação do nosso sistema.
    '''
    # Retorna uma resposta em formato JSON de boas-vindas
    return {"mensagem": "Você acessou a rota de autenticação"}


# Rota HTTP POST para cadastro de novos usuários (/auth/criar_conta)
@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuariosSchema, session: Session = Depends(pegar_sessao)):

    # Consulta no banco de dados para verificar se já existe um usuário cadastrado com o e-mail informado
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()

    # Se a consulta retornar algum usuário, lança um erro HTTP 400 (Bad Request)
    if usuario:
        raise HTTPException(status_code = 400, detail = "Usuário já existe.")

    # Se o usuário não existir, prossegue com o cadastro
    else:
        # Trata a senha ajustando a codificação UTF-8 e limitando a 72 bytes (limite padrão do algoritmo Bcrypt)
        senha_tratada = usuario_schema.senha.encode("utf-8")[:72].decode("utf-8", errors="ignore")

        # Gera o hash criptografado e seguro da senha
        senha_criptografada = bcrypt_context.hash(senha_tratada)
        
        # 3. Passa a senha CRIPTOGRAFADA para o Usuario (e não a senha pura)
        # Instancia o objeto do banco de dados com os dados recebidos da requisição
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        
        # Adiciona o novo objeto na fila de transação da sessão do banco
        session.add(novo_usuario)
        
        # Confirma e salva definitivamente as alterações no banco de dados
        session.commit()

        # Retorna uma mensagem de sucesso no formato JSON
        return {"mensagem": f"Usuário cadastrado com sucesso. {usuario_schema.nome} - {usuario_schema.email}"}


# Rota HTTP POST para autenticação e login de usuários (/auth/login)
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    # Busca no banco de dados o usuário correspondente ao e-mail informado no login
    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first()

    # Se o e-mail não for encontrado no banco de dados, interrompe e lança erro HTTP 400
    if not usuario:
        raise HTTPException(status_code = 400, detail = "Usuário não encontrado")

    # Se o usuário for encontrado, gera o token de autenticação
    else:
        # Chama a função de criar token passando o ID do usuário localizado
        acess_token = criar_token(usuario.id)
        
        # Retorna o token gerado e o tipo de autenticação (Bearer) em formato JSON
        return {"acess_token": acess_token, "token_type": "Bearer"}