import pytest
from pessoa_gato import *

@pytest.fixture
def pessoa():
	return Pessoa("Francisco José", 8226550394, "Teresina(PI)")

@pytest.fixture
def gato():
	return Gato(1.5, 3, "Malhado", "Vira-lata", "Saori Kido")

def test_pessoa_sem_gato(pessoa):
	assert pessoa.gato is None
	assert pessoa.gato_info == "Não possui gatos"

def test_gato_sem_dono(gato):
	assert gato.dono is None
	assert gato.dono_nome == "Sem dono"

def test_pessoa_adota_gato(pessoa, gato):
	mensagem = pessoa.adotar(gato)
	assert pessoa.gato.nome == "Saori Kido"
	assert gato.dono.nome == "Francisco José"
	assert mensagem == "Francisco José adotou Saori Kido!"

def test_substituir_gato(pessoa, gato):
	gato2 = Gato(3, 5, "Laranja", "Siamês", "Kinder Ovo")
	pessoa.adotar(gato)
	assert pessoa.gato.nome == "Saori Kido"
	assert gato.dono.nome == "Francisco José"
	mensagem = pessoa.adotar(gato2)
	assert pessoa.gato.nome == "Kinder Ovo"
	assert gato.dono.nome == "Francisco José"
	assert mensagem == "Francisco José adotou Kinder Ovo!"
