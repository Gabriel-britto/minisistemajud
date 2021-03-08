class Pessoa:
  def __init__(self, cpf, nome, processos = []):
    self._cpf= cpf #CPF da pessoa
    self._nome = nome #Nome da pessoa
    self._processos = processos #Processos atrelados a pessoa

  @property
  def cpf(self):
    return self._cpf
  @cpf.setter
  def cpf(self, novo_cpf):
    self._cpf= novo_cpf

  @property
  def nome(self):
    return self._nome
  @nome.setter
  def nome(self, novo_nome):
    self._nome =  novo_nome

  @property
  def processos(self):
    return self._processos
  @processos.setter
  def processos(self, novo_processo):
    self._processos = novo_processo

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

  def __str__(self):
    return "CPF: {}\nNome: {}\nProcessos: {}".format(self.cpf, self.nome, self.processos)