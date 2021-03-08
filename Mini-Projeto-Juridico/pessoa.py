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
  @property
  def num_decisoes(dec): #Deve ser True ou False e retornar a quantidade de processos que ja foram def ou ind
    return ""
  def custo_total(self): #Ainda não sei como fazer
    return self.custo
  def custo_total_adv(cod_oab):#Retornar o custo total dos processos da pessoa em que o advogado do código está envolvido.
    return
  def __str__(self):
    return "CPF: {}\nNome: {}\nProcessos: {}".format(self.cpf, self.nome, self.processos)