#!/usr/bin/python3

#    wordlist_generator Copyright (C) 2020  Gabriel Neves https://github.com/GabrielNeves18
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
##ghfdytdytddyd


#ghfdytdytddyd


def menu():
    """Esta def pergunta ao usuario o que ele quer realizar """
    
    escolha = input('O que você quer fazer? Combinar duas wordlist em uma ou criar uma? ')
    if escolha == 'combinar':
        primeiro = open(input('Digite o nome do 1º arquivo: '))
        segundo = open(input('Digite o nome do 2º arquivo: '))
        combinar_wordlist(primeiro, segundo)
    elif escolha == 'criar':
        nome_do_arquivo = open(input('Digite o nome do arquivo: '))
        criar_wordlist(nome_do_arquivo)
    else:
        print('Não exite essa opção, digite combinar ou criar')
        menu()
        
def combinar_wordlist(primeiro_arq, segundo_arq):
    """ Esta def combina duas lista, tirando as palavras iguais """
    
    arquivo = open(input('Qual é o nome da wordlist: '))
    arquivo.writelines(set(primeiro_arq).union(set(segundo_arq)))
    arquivo.close()

      
def criar_wordlist(arquivo):
    """ Cria uma wordlist com base numa lista """
    
    lista_completa = set(arquivo)
    senha = [] 
    New_file = input('Digite o nome do arquivo com as senhas: ')
    arq_novo = open(New_file,'a+')
    
    for linha in lista_completa:
        senha.append(linha.split('pass='))
    for linha in senha:
        del linha[0]
    
    for indice in senha:
        for i in indice:
            if i not in arq_novo:
                i = i.strip()
                arq_novo.writelines(i+'\n') 
    arq_novo.close()


menu()
