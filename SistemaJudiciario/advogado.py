class Advogado:
  def __init__(self, cod_oab, nome, processos = []):
    self._cod_oab = cod_oab
    self._nome_adv = nome
    self._processosadv = processos

  @property
  def cod_oab(self):
    return self._cod_oab
  @cod_oab.setter
  def cod_oab(self, novo_cod_oab):
    self._cod_oab = novo_cod_oab

  @property
  def nome_adv(self):
    return self._nome_adv
  @nome_adv.setter
  def nome_adv(self, novo_nome):
    self._nome_adv =  novo_nome

  @property
  def processos(self):
    return self._processosadv
  @processos.setter
  def processos(self, novo_processo):
    self._processosadv = novo_processo
  def lista_clientes():
    for i in range(len(lista)):
      return lista[i].pessoa.nome
  def __str__(self):
    return "OAB: {}, Nome: {}, Processos: {}".format(self.cod_oab, self.nome_adv, self.processos)