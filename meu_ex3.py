# Um programa de carro qualquer...



from os import system

def menu():
  system('cls')
  print('Olá esse é o menu, Esse programa serve para você cadastrar, alterar, listar, excluir, adicionar, listar um carro a sua loja, Então vamos lá!!')
  print('-'*30)
  print('-'*30)
  print('1) Cadastrar')
  print('2) Alterar')
  print('3) Listar tudo')
  print('4) Excluir')
  print('5) Listar apenas os nomes dos carros cadastrados')
  print('6) Listar todos os dados de todos os carros cadastrados')
  print('7) Listar os dados de um carro especifico')
  print('8) Verificar se um carro existe na lista')
  print('0) Sair')


def cadastrar():
  system('cls')
  print('Vamos cadastrar um carro novo a sua lista de carros da loja: ')
  voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
  if voltar_menu == 1:
    print('Vamos voltar pro menu agora!!')
    system('pause')
    menu()
  if voltar_menu == 2:
    carro_cadastrar = input('Digite o nome do carro que você quer cadastrar: ')
    ano = input('Digite o ano de fabricação do carro: ')
    preco = (input('Digite quanto você pagou nele: '))
    nome = input('Digite o nome da pessoa que te vendeu o carro: ')
    carros[carro_cadastrar] = {'ano do carro': ano,'preço do carro':preco,'nome da pessoa que te vendeu o carro':nome}
    menu()

def alterar():
  system('cls')
  if carros == {} :
    print('A lista de carros ainda está vázia')
    system('pause')
    menu()
  else:
    print('Vamos alterar um carro: ')
    voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
    if voltar_menu == 1:
      print('Vamos voltar pro menu agora!!')
      system('pause')
      menu()
    if voltar_menu == 2:
      print('Esses são os carros e seus respectivos dados: ')
      print(carros)
      carro = input('Digite qual carro você quer alterar os dados dele: ')
      carro_dado = input('Digite qual dado do carro você quer alterar: ')
      dado_novo = input('Digite qual novo dado você quer colocar: ')
      carros[carro][carro_dado] = dado_novo
      print('Dado alterado com sucesso, esses são os dados novos do carro que você quis alterar: ')
      print(carros[carro])
      system('pause')
      menu()

def listar():
  system('cls')
  if carros == {} :
    print('A lista de carros ainda está vázia')
    system('pause')
    menu()
  else:
    print('Vamos listar todos os carros cadastrados da sua loja e seus dados: ')
    voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
    if voltar_menu == 1:
      print('Vamos voltar pro menu agora!!')
      system('pause')
      menu()
    if voltar_menu == 2:
      print(carros)
      system('pause')
      menu()

def excluir():
  system('cls')
  if carros == {} :
    print('A lista de carros ainda está vázia')
    system('pause')
    menu()
  else:
    print('Vamos excluir o carro que você desejar e seus respectivos dados!!')
    voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
    if voltar_menu == 1:
      print('Vamos voltar pro menu agora!!')
      system('pause')
      menu()
    if voltar_menu == 2:
      print('Esses são os carros que nossa loja possui: ')
      for carro in carros:
        print(carro)
      carro = input('Digite o carro que você quer excluir da loja: ')
      del carros[carro]
      print('Carro excluido, essa é a nova lista de carros da loja: ')
      for carro in carros:
        print(carro)
      system('pause')
      menu()

def listar_carros():
  system('cls')
  if carros == {} :
    print('A lista de carros ainda está vázia')
    system('pause')
    menu()
  else:
    print('Esses são os carros da loja: ')
    voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
    if voltar_menu == 1:
      print('Vamos voltar pro menu agora!!')
      system('pause')
      menu()
    if voltar_menu == 2:
      for carro in carros:
        print(carro)
      system('pause')
      menu()

def listar_dados():
  system('cls')
  if carros == {} :
    print('A lista de carros ainda está vázia')
    system('pause')
    menu()
  else:
    print('Esses são os dados de todos os carros da loja: ')
    voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
    if voltar_menu == 1:
      print('Vamos voltar pro menu agora!!')
      system('pause')
      menu()
    if voltar_menu == 2:
      for carro in carros:
        print(carros[carro])
        system('pause')
        menu()


def dados_unico_carro():
  system('cls')
  if carros == {} :
    print('A lista de carros ainda está vázia')
    system('pause')
    menu()
  else:
    print('Esses são os carros da loja: ')
    voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
    if voltar_menu == 1:
      print('Vamos voltar pro menu agora!!')
      system('pause')
      menu()
    if voltar_menu == 2:
      for carro in carros:
        print(carro)
      carro = input('Vamos lá, aqui vamos mostrar os dados do carro que você escolher, digite o nome do carro que você quer ver   seus dados: ')
      print('Esses são os dados do carro que você escolheu: ')
      print(carros[carro])
      system('pause')
      menu()


def verificar():
  system('cls')
  if carros == {} :
    print('A lista de carros ainda está vázia')
    system('pause')
    menu()
  else:
    voltar_menu = int(input('Caso queira continuar no processo digite 2 e caso queira voltar pro menu digite 1: '))
    if voltar_menu == 1:
      print('Vamos voltar pro menu agora!!')
      system('pause')
      menu()
    if voltar_menu == 2:
      carro = input('Vamos verificar se o carro que você quer consultar, ver se ele existe na loja, digite o nome do carro que você quer ver se possui na loja: ')
      if carro not in carros:
        print('Esse carro não possui na loja')
        system('pause')
        menu()
      elif carro in carros:
        print('O carro que você digitou possui na loja')
        system('pause')
        menu()


def main():
  number = int(input('Digite a alternativa desejada do menu: '))
  while number != -1:
    if number == 1:
      cadastrar()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 2:
      alterar()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 3:
      listar()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 4:
      excluir()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 5:
      listar_carros()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 6:
      listar_dados()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 7:
      dados_unico_carro()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 8:
      verificar()
      number = int(input('Digite a alternativa desejada do menu: '))

    elif number == 0:
      print('Você saiu do programa até mais!!')
      system('pause')
      system('cls')
      break


menu()
carros = {}
main()
