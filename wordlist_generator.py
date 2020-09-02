#!/usr/bin/python3

#    wordlist_generator Copyright (C) 2020  Gabriel Neves https://github.com/GabrielNeves18
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#

def menu():
    escolha = input("O que você quer fazer? Combinar duas wordlist em uma ou criar uma? ")
    if escolha == "combinar":
        primeiro = open(input("Digite o nome do 1º arquivo: ")+'.txt')
        segundo = open(input("Digite o nome do 2º arquivo: ")+'.txt')
        combinar(primeiro, segundo)
    elif escolha == "criar":
        nome_do_arquivo = open(input("Digite o nome do arquivo: ")+'.txt')
        somente_senha(nome_do_arquivo)
    else:
        print("Não exite essa opção, digite combinar ou criar")
        menu()
        
def combinar(primeiro_arq, segundo_arq):
    arquivo = open(input("Qual é o nome da wordlist: ")+'.txt', 'a+')
    conj1 = set(primeiro_arq)
    conj2= set(segundo_arq)
    arquivo.writelines(conj1.union(conj2))
    
    arquivo.close()
 
def somente_senha(arquivo):
    lista_completa = [] # recebe sublista
    lista2 = [] 
    New_file = input("Digite o nome do arquivo com as senhas: ")
    arq_novo = open(New_file+'.txt', 'a+')

    for linha in arquivo: # Adiciona toda as linhas do arquivo que contém a string 'pass' na lista_pass
        if 'pass' in linha:
            lista_completa.append(linha.split(' ')) # split quebra a palavra no espaço em branco " "

    for sub_lista in lista_completa: # Adiciona na lista2 a chave e o valor
        for string in sub_lista:
            if 'pass' in string:
                lista2.append(string.split('='))


    for linha in sorted(lista2): # Adiciona ao dicionario a chave/valor
        dici = {}
        for i in linha:
            dici.setdefault(i, linha[1])
            if '\n' not in dici[i]: # verifica se existe um quebra linha
                dici[i] = dici[i]+'\n'

        arq_novo.writelines(dici[i]) # Escreve no arquivo a senha

    arq_novo.close()

print("OLA")
menu()
