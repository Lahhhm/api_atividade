#Aonde está as classes que vão redirencionar o Banco de dados

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship  #Responsaveis por criar a seções: Consulta, Alterac;
from sqlalchemy.ext.declarative import declarative_base

#Necessário para acessar o banco de dados e realizar alterações e consultas
engine = create_engine('sqlite:///atividade.db', convert_unicode=True)  #Criando o Banco de Dados
db_session = scoped_session(sessionmaker(autocommit=False,     #comentar automatico
                                         bind=engine))   #Tem que passar o Banco para abrir a secao

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'   #Nome da Tabela no Banco
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)   #Index para deixar a consulta mais rapida
    idade = Column(Integer)

    def __repr__(self):    #Quando mandar imprimir o objeto vai chamar esta funcao, representacao da class
        return '<Pessoa {}>'.format(self.nome) #Imprime somente o nome ao chamar imprimir

    def save(self):   #Salvar no Banco de Dados
        db_session.add(self)
        db_session.commit()

    def delete(self):  #Deletar registros do banco
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))   #Relacionando Atividade com tabela: pessoa
    pessoa = relationship("Pessoas")  #Relacionando: pessoa com a class Pessoas

    def __repr__(self):    #Quando mandar imprimir o objeto vai chamar esta funcao, representacao da class
        return '<Atividades {}>'.format(self.nome) #Imprime somente o nome ao chamar imprimir

    def save(self):   #Salvar no Banco de Dados
        db_session.add(self)
        db_session.commit()

    def delete(self):  #Deletar registros do banco
        db_session.delete(self)
        db_session.commit()



def init_db():
    Base.metadata.create_all(bind=engine)  #Comando para criar o banco de dados

if __name__ == '__main__':
    init_db()
