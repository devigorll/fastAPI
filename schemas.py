# ARQUIVO: schemas.py

# OBJETIVO: 

# Este arquivo define os Schemas do Pydantic utilizados na aplicação.
# Ele é responsável por:
# 1. Definir os modelos de validação e estruturação dos dados de entrada (Data Transfer Objects - DTOs).
# 2. Garantir que as requisições enviadas pelo cliente possuam o formato e os tipos corretos de dados.
# 3. Configurar a conversão automática entre os objetos do ORM (SQLAlchemy) e os schemas do Pydantic.


# Importa a classe base do Pydantic para criação de schemas de validação de dados
from pydantic import BaseModel

# Importa o tipo de anotação Optional do Python para indicar campos que não são obrigatórios
from typing import Optional


# Schema para validação dos dados no cadastro de novos usuários
class UsuariosSchema(BaseModel):
    nome: str              # Nome do usuário (obrigatório, tipo texto)
    email: str             # Endereço de e-mail (obrigatório, tipo texto)
    senha: str             # Senha de acesso (obrigatória, tipo texto)
    ativo: Optional[bool]  # Status da conta (opcional, tipo booleano: True/False)
    admin: Optional[bool]  # Permissão de administrador (opcional, tipo booleano: True/False)

    # Configuração interna do Pydantic
    class Config:
        from_attributes = True  # Permite mapear automaticamente atributos vindos de modelos ORM (como SQLAlchemy)


# Schema para validação dos dados na criação de um novo pedido
class PedidoSchema(BaseModel):
    usuario: int  # ID do usuário vinculado ao pedido (obrigatório, tipo inteiro)

    # Configuração interna do Pydantic
    class Config:
        from_attributes = True  # Permite conversão direta entre modelos do banco e o schema


# Schema para validação das credenciais enviadas na rota de login/autenticação
class LoginSchema(BaseModel):
    email: str  # E-mail digitado no login (obrigatório, tipo texto)
    senha: str  # Senha digitada no login (obrigatória, tipo texto)

    # Configuração interna do Pydantic
    class Config:
        from_attributes = True  # Permite leitura dinâmica de objetos