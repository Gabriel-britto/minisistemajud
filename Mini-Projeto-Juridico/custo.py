class Custo:
  def __init__(self, data, descricao_custo, valor):
    self._data = data
    self._descricao_custo = descricao_custo
    self._valor = valor
  @property
  def data(self):
    return self._data
  @data.setter
  def data(self, nova_data):
    self._data= nova_data
  @property
  def descricao_custo(self):
    return self._descricao_custo
  @descricao_custo.setter
  def descricao_custo(self, nova_descricao_custo):
    self._descricao_custo = nova_descricao_custo
  @property
  def valor(self):
    return self._valor
  @valor.setter
  def valor(self, novo_valor):
    if novo_valor >= 0:
      self.valor = novo_valor
  def __str__(self):
    return "Data: {}, Descrição: {}, Valor: R$:{}".format(self.data, self.descricao_custo, self.valor)
