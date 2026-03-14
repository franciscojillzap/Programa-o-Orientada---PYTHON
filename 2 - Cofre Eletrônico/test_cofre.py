import pytest
from cofre import *

# Fixture que cria um cofre novo antes de cada teste
@pytest.fixture
def cofre():
    return Cofre_Eletronico(senha="1234")


def test_abrir_com_senha_correta(cofre):
    assert cofre.abrir_cofre("1234") == "Cofre aberto com sucesso!"
    assert cofre.estado == "aberto"


def test_abrir_com_senha_incorreta(cofre):
    resposta = cofre.abrir_cofre("0000")
    assert "Senha incorreta" in resposta
    assert cofre.tentativas_restantes == 2


def test_bloqueio_apos_tres_erros(cofre):
    cofre.abrir_cofre("0000")
    cofre.abrir_cofre("1111")
    resposta = cofre.abrir_cofre("2222")
    assert resposta == "Número de tentativas esgotado. Cofre bloqueado."
    assert cofre.tentativas_restantes == 0


def test_fechar_cofre(cofre):
    cofre.abrir_cofre("1234")
    resposta = cofre.fechar_cofre()
    assert resposta == "Cofre fechado."
    assert cofre.estado == "fechado"
    


def test_resetar_tentativas_aberto(cofre):
    cofre.abrir_cofre("1234")
    cofre.tentativas_restantes = 1
    resposta = cofre.resetar_tentativas()
    assert resposta == "Tentativas resetadas para 3."
    assert cofre.tentativas_restantes == 3


def test_resetar_tentativas_fechado(cofre):
    resposta = cofre.resetar_tentativas()
    assert resposta == "Não é possível resetar as tentativas enquanto o cofre estiver fechado."
