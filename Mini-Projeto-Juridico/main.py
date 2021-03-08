#Fazer os métodos
#Funcionalidade extra: Modo teste: Adiciona Objetos completos para teste das funcionalidades 
from processo import Processo
from advogado import Advogado
from audiencia import Audiencia
from custo import Custo
from pessoa import Pessoa

def num_decisoes(cpf):
  numdef = numindef = 0
  print("Contagem:")
  for i in range(len(lista)):
    if lista[i].pessoa.cpf == cpf:
      if lista[i].decisao == "deferido":
        numdef += 1
      elif lista[i].decisao == "indeferido":
        numindef += 1
  return "Vezes deferido: {}\nVezes indeferido: {}".format(numdef,numindef)

def lista_clientes(codigo):
  clientes = []
  for i in range(len(lista)):
    if lista[i].advogado.cod_oab == codigo:
      cc= lista[i].pessoa.nome
      clientes.append(cc)
  return clientes

def custo_total_pessoa(cpf):
  totalpessoa = 0
  for i in range(len(lista)):
    if lista[i].pessoa.cpf == valorcpf:
      totalpessoa += lista[i].custo._valor
  return totalpessoa

def custo_total_adv(codigo):
  totaladvogado = 0
  for i in range(len(lista)):
    if lista[i].advogado.cod_oab == codigo:
      totaladvogado += lista[i].custo._valor
  return totaladvogado

def busca_processo(cpfpessoa):
  if len(lista) > 0:
    buscatempocpf = []
    for i in range(len(lista)):
      if buscprocessocpf == lista[i].pessoa.cpf:
        descricoescpf = ("Audiencia {} {}: {}\nRecomendação: {}".format(i+1,lista[i].audiencias.data_aud,lista[i].descricao, lista[i].audiencias.recomendacao))
        buscatempocpf.append(descricoescpf)
    return buscatempocpf

def audiencias_temp(buscprocesso):
  if len(listadura) > 0:
    buscatempo = []
    for i in range(len(lista)):
      if buscprocesso <= listadura[i].duracao:
        descricoes = ("Audiencia {} {}: {}\nRecomendação: {}".format(i+1,lista[i].audiencias.data_aud,lista[i].descricao, lista[i].audiencias.recomendacao))
        buscatempo.append(descricoes)
    return buscatempo

def modo_teste():
  teste1 = Processo("Latrocinio",Custo("23/05/2020","Abertura do processo",500),"deferido", "PROCESSO DEFERIDO AGUARDANDO FINALIZAÇÃO",Pessoa("111.222.333-44", "João da silva","1,2,3"),Advogado(5552,"Joaquim S. Cavalcante","1,2"),Audiencia("28/05/2020","Arquivamento do processo",30))
  teste2 = Processo("Extorsão",Custo("10/09/2010","Danos",5000),"deferido", "PROCESSO DEFERIDO AGUARDANDO FINALIZAÇÃO",Pessoa("111.222.444-55", "José tavares","1,2,3"),Advogado(3452,"João Cavalcante","1,2"),Audiencia("10/10/2010","Liberdade provisória",35))
  teste1_audiencia = Audiencia("23/05/2002","Arquivamento do processo",30)
  teste1_custo = Custo("15/03/2020","Abertura do processo",500)
  teste2_audiencia = Audiencia("10/10/2010","Liberdade provisória",35)
  teste2_custo = Custo("10/09/2010","Danos",5000)
  lista.append(teste1)
  listadura.append(teste1_audiencia)
  custototal.append(teste1_custo)
  lista.append(teste2)
  listadura.append(teste2_audiencia)
  custototal.append(teste2_custo)

lista = []
listadura = []
custototal = []
advogados = []
menu = 0
totalprocessos = 0

while menu != 9:
  print("-"*15,"Sistema Jurídico","-"*15)
  painel = "1 - Cadastrar Processo\n2 - Menu de buscas\n3 - Imprimir descrição das audiências\n4 - Buscar clientes de Advogado\n5 - Custo total\n6 - Consulta de Def/Ind\n7 - Imprimir todos os processos cadastrados\n8 - Objetos de teste\n9 - Finalizar\n> "
  menu = int(input(painel))

  if menu == 1:
    print("-"*15,"Cadastro de processos:","-"*15)
    vezes = int(input("Quantos processos deseja cadastrar? "))
    for i in range(vezes):
      print("-"*15,"Processo {}".format(i+1),"-"*15)
      print("-Dados do Processo-")
      descricao = input("Descrição do Processo: ")
      data = input("Data(DD/MM/YEAR): ")
      print("-Dados de custo-")
      custo_descricao = input("Descrição do custo: ")
      valor = int(input("Valor:"))
      decisao = input("Digite a decisão(Deferido/Indeferido):").lower()
      status = input("Status do processo: ")
      print("-Dados da Pessoa-")
      cpf = input("CPF da pessoa: ")
      nome = input("Nome da pessoa: ")
      processos = i #metodo que retorne os processos atrelados a pessoa
      print("-Dados do Advogado-")
      cod_oab = int(input("Digite o Código da OAB: "))
      nome_adv = input("Digite o nome do Advogado: ")
      processos_adv = i #metodo que retorna os processos atrelados ao advogado
      data_aud = input("Data da Audiência(DD/MM/YEAR): ")
      recomendacao = input("Recomendação: ")
      duracao = int(input("Duração da Audiência(Minutos): "))
      adv = Advogado(cod_oab,nome_adv,processos_adv)
      a = Audiencia(data_aud,recomendacao,duracao)
      c = Custo(data,custo_descricao,valor)
      p = Processo(descricao,c,decisao,status,Pessoa(cpf,nome,processos),adv,a)
      advogados.append(adv)
      listadura.append(a)
      lista.append(p)
      custototal.append(c)


  elif menu == 2:
    print("-"*15,"Menu de Buscas","-"*15)
    print("1 - Busca por duração\n2 - Busca por CPF\n3 - Sair\n ")
    menu_busca = 0
    while menu_busca != 3:
      menu_busca = int(input("> "))
      if menu_busca == 1:
        buscprocesso = int(input("Digite a duração do Processo: "))
        if len(listadura) > 0:
          resposta = audiencias_temp(buscprocesso)
          for i in range(len(resposta)):
            print(resposta[i])
        else:
          print("Nenhum processo encontrado")
          reset = input("Pressione Enter para continuar")
      elif menu_busca == 2:
        buscprocessocpf = input("Digite o CPF atrelado ao processo: ")
        if len(lista) > 0:
          printar = busca_processo(buscprocessocpf)
          for i in range(len(printar)):
            print(printar[i])
        else:
          print("Processo não encontrado")
  elif menu == 3:
    if len(lista)>0:
      for i in range(len(lista)):
        print("Processo {}:".format(i+1),lista[i]._descricao)
    else:
      print("Nenhum processo cadastrado")
      reset = input("Pressione Enter para continuar")


  elif menu == 4:
    codigo = int(input("Código da OAB:"))
    print("Clientes:",lista_clientes(codigo))


  elif menu == 5:
    print("-"*15,"Menu de Custo","-"*15)
    print("1 - Custo total dos processos\n2 - Custo dos processos de um advogado\n3 - Custo do processo da pessoa\n4 - Sair\n")
    menu_custo = 0
    while menu_custo != 4:
      menu_custo = int(input("> "))

      if menu_custo == 1:
        if len(custototal) > 0:
          for i in range(len(custototal)):
            totalprocessos += custototal[i]._valor
          print("Custo total dos processos: {}".format(totalprocessos))
        else:
          print("Nenhum processo encontrado")
          reset = input("Pressione Enter para continuar")
        
      elif menu_custo == 2:
        codoab = int(input("Digite o OAB do advogado: "))
        valoradv = custo_total_adv(codoab)
        print("Custo total dos processos do advogado: {}".format(valoradv))

      elif menu_custo == 3:
        valorcpf = input("Digite o CPF da pessoa: ")
        valorpessoa = custo_total_pessoa(valorcpf)
        print("Custo total dos processos da pessoa: {}".format(valorpessoa))

  elif menu == 6:
    pesqcpf = input("Digite o CPF de quem você deseja pesquisar:")
    print(num_decisoes(pesqcpf))
    
  elif menu == 7:
    print("-"*15,"Processos Cadastrados:","-"*15)
    for i in range(len(lista)):
      print(lista[i],"\n")

  elif menu == 8:
    modo_teste()
    print("Objetos adicionados.")

  elif menu == 9:
    print("-"*15,"Programa finalizado","-"*15)

  else:
    print("Opção inválida. Tente novamente")