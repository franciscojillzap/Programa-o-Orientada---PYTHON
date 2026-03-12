from card import *
import pytest

@pytest.fixture
def true_card():
    return Card("Mago Negro", "monstro", 2500, 2100)

def false_card():
    return Card("Pote da Merenda", "Refeição")


def test_construtor(true_card):
    assert true_card.nome == "Mago Negro"
    assert true_card.tipo == "monstro"
    assert true_card.ATK == 2500
    assert true_card.DEF == 2100

def test_invocar(true_card, false_card):
    assert true_card.invocar() == "Eu invoco Mago Negro! Em Modo de Ataque!"
    assert false_card.invocar() == "Tipo de Card desconhecido."

def test_detalhes(true_card):
    assert true_card.detalhes() == "Card: Mago Negro\nTipo: monstro\nATK: 2500\nDEF: 2100"

def test_aumentar_atributos(true_card, false_card):
    assert true_card.aumentar_atributos() == "Mago Negro\nATK: 3200\nDEF: 2800"
    assert false_card.aumentar_atributos() == "Este Card não é um monstro!"
