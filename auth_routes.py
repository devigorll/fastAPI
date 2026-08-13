from fastapi import APIRouter, Depends, HTTPException, status
from models import Usuario, db
from sqlalchemy.orm import sessionmaker
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuariosSchema
from sqlalchemy.orm import Session 

auth_router = APIRouter(prefix = "/auth", tags = ["auth"])

@auth_router.get("/")
async def home():

    '''
        Essa é a rota padrão de autenticação do nosso sistema.
    '''

    return {"mensagem": "Você acessou a rota de autenticação"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuariosSchema, session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()

    if usuario:
        raise HTTPException(status_code = 400, detail = "Usuário já existe.")

    else:
        senha_tratada = usuario_schema.senha.encode("utf-8")[:72].decode("utf-8", errors="ignore")

        senha_criptografada = bcrypt_context.hash(senha_tratada)
        
        # 3. Passa a senha CRIPTOGRAFADA para o Usuario (e não a senha pura)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        
        session.add(novo_usuario)
        session.commit()

        return {"mensagem": f"Usuário cadastrado com sucesso. {usuario_schema.nome} - {usuario_schema.email}"}