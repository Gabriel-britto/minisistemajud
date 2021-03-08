class Processo:
  def __init__(self, descricao, custo, decisao, status, pessoa, advogado, audiencias):
    self._descricao = descricao #String com a descrição do Processo  
    self._custo = custo #Custo do Processo
    self._decisao = decisao #Decisão final do processo: Deferido ou intedeferido
    self._status = status #String de status do descorrer do processo
    self._pessoa = pessoa #Pessoa do processo
    self._advogado = advogado #Advogado do Processo
    self._audiencias = audiencias #Lista de audiencias

  @property
  def descricao(self):
    return self._descricao
  @descricao.setter
  def descricao(self, nova_descricao):
    self._descricao= nova_descricao

  @property
  def custo(self):
    return self._custo
  @custo.setter
  def custo(self, novo_custo):
    if novo_custo>=0:
      self._custo= novo_custo

  @property
  def decisao(self):
    return self._decisao
  @decisao.setter
  def decisao(self, nova_decisao):
    self.decisao = nova_decisao

  @property
  def status(self):
    return self._status
  @status.setter
  def status(self,novo_status):
    self.status = novo_status

  @property
  def pessoa(self):
    return self._pessoa
  @pessoa.setter
  def pessoa(self, nova_pessoa):
    self._pessoa= nova_pessoa

  @property
  def advogado(self):
    return self._advogado
  @advogado.setter
  def advogado(self, novo_advogado):
    self._advogado = novo_advogado
    
  @property
  def audiencias(self):
    return self._audiencias
  @audiencias.setter
  def audiencias(self, nova_audiencia):
    self.audiencias = nova_audiencia

  def audiencias_temp(buscprocesso):
    if len(listadura) > 0:
      buscatempo = []
      for i in range(len(lista)):
        if buscprocesso <= listadura[i].duracao:
          descricoes = ("Audiencia {} {}: {}\nRecomendação: {}".format(i+1,lista[i].audiencias.data_aud,lista[i].descricao, lista[i].audiencias.recomendacao))
          buscatempo.append(descricoes)
      return buscatempo
  def __str__(self):
    return "Processo:\nDescrição: {}\nCusto: {}\nDecisão: {}\nStatus: {}\nPessoa: {}\nAdvogado(a): {}\nAudiencias: {}".format(self._descricao, self._custo, self._decisao, self._status, self._pessoa, self._advogado, self._audiencias)