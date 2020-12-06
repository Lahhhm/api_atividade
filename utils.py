from models import Pessoas

#Insere dados na Tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Rose', idade=20)
    print(pessoa)   # Esta chamado o metodo criado para imprimir na classe
    pessoa.save()   #Sem esse comando não é adicionado no banco, chamando metodo da class Pessoas

#Realiza consulta na Tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)  #Imprime todas as pessoas da tabela
    pessoa = Pessoas.query.filter_by(nome='Yama').first()
    print(pessoa.idade)  #Imprima somente idade da pessoa
    print(pessoa)

#Realiza alteracao na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(id=2, nome='Yama').first() #Filtro para buscar no banco/First: Primeiro Registro
    pessoa.idade = 21
    pessoa.nome = 'Felipe'
    pessoa.save()

#Realiza exclusao na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rose').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #consulta_pessoas()
    #exclui_pessoa()
    consulta_pessoas()