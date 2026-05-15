import pytest
from funcionario_dependente import *

@pytest.fixture
def f1():
	return Funcionario("Carlos")

def test_adicionar_dependente(f1):
	f1.adicionar_dependente("Francisco José", 21, "Solteiro", "Empregado")
	f1.adicionar_dependente("Janaína Lima", 39, "Casada", "Desempregada")
	
	lista = f1.dependentes

	assert len(lista) == 2
	assert lista[0].nome == "Francisco José"
	assert lista[1].nome == "Janaína Lima"

def test_remover_dependente_existente(f1):
	f1.adicionar_dependente("Francisco José", 21, "Solteiro", "Empregado")
	f1.adicionar_dependente("Janaína Lima", 39, "Casada", "Desempregada")

	resultado = f1.remover_dependente("Francisco José")

	assert resultado == "O usuário Francisco José foi removido da lista de dependentes."

def test_remover_dependente_inexistente(f1):
	f1.adicionar_dependente("Francisco José", 21, "Solteiro", "Empregado")
	f1.adicionar_dependente("Janaína Lima", 39, "Casada", "Desempregada")
	f1.remover_dependente("Francisco José")

	resultado = f1.remover_dependente("Francisco José")

	assert resultado == "Usuário Francisco José não encontrado."

def test_lista_sem_dependentes(f1):
	lista_vazia = f1.listar_dependentes()

	assert lista_vazia == "O funcionário Carlos não possui dependentes registrados."

def test_lista_com_dependentes(f1):
	f1.adicionar_dependente("Francisco José", 21, "Solteiro", "Empregado")
	f1.adicionar_dependente("Janaína Lima", 39, "Casada", "Desempregada")
	
	lista = f1.listar_dependentes()

	assert "Francisco José" in lista
	assert "Janaína Lima" in lista