class Dependente:
	def __init__(self, nome, idade, estado, situacao):
		self.__nome = nome
		self.__idade = idade
		self.__estado = estado
		self.__situacao = situacao

	@property
	def nome(self):
		return self.__nome

	@property
	def idade(self):
		return self.__idade
	
	@property
	def estado(self):
		return self.__estado

	@property
	def situacao(self):
		return self.__situacao

	@estado.setter
	def estado(self, novo_estado):
		estados_civis = ["Solteiro", "Casado", "Divorciado", "Viúvo", "Solteira", "Casada", "Divorciada", "Viúva"]

		if novo_estado in estados_civis:
			self.__estado = novo_estado

	@situacao.setter
	def situacao(self, nova_situacao):
		situacao_trabalho = ["Empregado", "Desempregado", "Desalentado", "Empregada", "Desempregada", "Desalentada"]

		if nova_situacao in situacao_trabalho:
			self.__situacao = nova_situacao

	def __repr__(self):
		return f"Dependente({self.__nome}, {self.__idade}, {self.__estado}, {self.__situacao})"
	
	def __del__(self):
		print(f"O usuário dependente {self.nome} foi excluído do banco de dados!")
	

class Funcionario:
	def __init__(self, nome):
		self.__nome = nome
		self.__dependentes = []

	@property
	def nome(self):
		return self.__nome

	@property
	def dependentes(self):
		return self.__dependentes[:]
	

	def adicionar_dependente(self, nome, idade, estado, situacao):
		self.__dependentes.append(Dependente(nome, idade, estado, situacao))

	def remover_dependente(self, nome_busca):
		for dependente in self.__dependentes:
			if dependente.nome == nome_busca:
				self.__dependentes.remove(dependente)
				return f"O usuário {dependente.nome} foi removido da lista de dependentes."
		else:
			return f"Usuário {nome_busca} não encontrado."
				

	def listar_dependentes(self):
		if not self.__dependentes:
			return f"O funcionário {self.nome} não possui dependentes registrados."
		else:
			resultado = f"Lista de dependentes do funcionário {self.nome}:"
			for dependente in self.__dependentes:
				resultado += f"\n{dependente.nome}"
			return resultado

	def __del__(self):
		print(f"O funcionário {self.nome} foi despedido!")