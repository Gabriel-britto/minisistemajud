class Audiencia:
  def __init__(self, data_aud, recomendacao, duracao):
    self._data_aud = data_aud
    self._recomendacao = recomendacao
    self._duracao = duracao
  @property
  def data_aud(self):
    return self._data_aud
  @data_aud.setter
  def data_aud(self, nova_data_aud):
    self._data_aud = nova_data_aud
  @property
  def recomendacao(self):
    return self._recomendacao
  @recomendacao.setter
  def recomendacao(self, nova_recomendacao):
    self._recomendacao = nova_recomendacao
  @property
  def duracao(self):
    return self._duracao
  @duracao.setter
  def duracao(self, nova_duracao):
    if nova_duracao > 0:
      self._duracao = nova_duracao
  def __str__(self):
    return "Data: {}, Recomendacao: {}, Duração: {}min(s)".format(self.data_aud, self.recomendacao, self.duracao)