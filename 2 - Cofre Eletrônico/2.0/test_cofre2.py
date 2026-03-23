import pytest
from cofre2 import *

# Fixture que cria um cofre novo antes de cada teste
@pytest.fixture
def cofre():
    return Cofre_Eletronico(senha="1234", codigo_mestre="admin")

# Testes aplicados ao método ABRIR_COFRE
def test_abrir_com_senha_correta(cofre):
    assert cofre.abrir_cofre("1234") == "Cofre aberto com sucesso!"
    assert cofre.estado == "aberto"
def test_abrir_com_senha_incorreta(cofre):
    resposta = cofre.abrir_cofre("0000")
    assert "Senha incorreta" in resposta
    assert cofre.tentativas == 2
def test_bloqueio_apos_tres_erros(cofre):
    cofre.abrir_cofre("0000")
    cofre.abrir_cofre("1111")
    resposta1 = cofre.abrir_cofre("2222")
    resposta2 = cofre.abrir_cofre("3333")
    assert resposta1 == "Número de tentativas esgotado. Cofre bloqueado."
    assert resposta2 == "Cofre bloqueado! Use o código mestre!"
    assert cofre.estado == "bloqueado"
    assert cofre.tentativas == 0

# Testes aplicados ao método FECHAR_COFRE
def test_fechar_cofre(cofre):
    cofre.abrir_cofre("1234")
    resposta = cofre.fechar_cofre()
    assert resposta == "Cofre fechado."
    assert cofre.estado == "fechado"

# Testes aplicados ao método RESETAR_TENTATIVAS
def test_resetar_tentativas_aberto(cofre):
    cofre.abrir_cofre("1234")
    cofre.tentativas_restantes = 1
    resposta = cofre.resetar_tentativas()
    assert resposta == "Tentativas resetadas para 3."
    assert cofre.tentativas == 3    
def test_resetar_tentativas_fechado(cofre):
    resposta = cofre.resetar_tentativas()
    assert resposta == "Não é possível resetar as tentativas enquanto o cofre estiver fechado."

# Testes aplicados ao método TROCAR_SENHA
def test_trocar_senha_com_sucesso(cofre):
    cofre.abrir_cofre("1234")
    resposta = cofre.trocar_senha("1234", "adm123")
    assert resposta == "Senha alterada com sucesso!"
    assert cofre.senha == "adm123"
def test_trocar_senha_cofre_fechado(cofre):
    resposta = cofre.trocar_senha("1234", "adm123")
    assert resposta == "A senha só pode ser alterada se o cofre estiver aberto!"
def test_trocar_senha_poucos_caracteres(cofre):
    cofre.abrir_cofre("1234")
    resposta = cofre.trocar_senha("1234", "adm")
    assert resposta == "A nova senha deve possuir pelo menos 6 caracteres!"
def test_trocar_senha_sem_numero(cofre):
    cofre.abrir_cofre("1234")
    resposta = cofre.trocar_senha("1234", "baitola")
    assert resposta == "A nova senha deve conter pelo menos um número!"

# Testes aplicados ao método DESBLOQUEAR_COFRE
def test_desbloquear_cofre_com_sucesso(cofre):
    cofre.estado = "bloqueado"
    resposta = cofre.desbloquear_cofre("admin")
    assert resposta == "Cofre desbloqueado!"
    assert cofre.estado == "aberto"
    assert cofre.tentativas == 3
def test_desbloquear_cofre_sem_bloqueio(cofre):
    resposta = cofre.desbloquear_cofre("admin")
    assert f"O cofre não encontra-se bloqueado. Seu estado atual é {cofre.estado}!" in resposta
def test_desbloquear_cofre_codigo_mestre_incorreto(cofre):
    cofre.estado = "bloqueado"
    assert cofre.desbloquear_cofre("pegasus") == "Código mestre incorreto."
    
