import pytest
from radio import *

# Fixture que cria um cofre novo antes de cada teste
@pytest.fixture
def radio():
    return RadioFM(100, estacoes)

# Testes aplicados ao método LIGAR
def test_ligar_radio_com_antena_desabilitada(radio):
    radio.antena_habilitada == False
    assert radio.ligar() == "O rádio está ligado."
    assert radio.ligado == True
    assert radio.volume == 0
    assert radio.estacao_atual == None
    assert radio.frequencia_atual == None
def test_ligar_radio_com_antena_habilitada(radio):
    radio.antena_habilitada = True
    assert radio.ligar() == "O rádio está ligado na estação: Cocais"
    assert radio.ligado == True
    assert radio.volume == 0
    assert radio.estacao_atual == "Cocais"
    assert radio.frequencia_atual == 89.5
    
# Testes aplicados ao método DESLIGAR
def test_desligar_radio_ligado(radio):
    radio.ligar()
    assert radio.desligar() == "O rádio foi desligado."
    assert radio.ligado == False
    assert radio.volume == None
    assert radio.estacao_atual == None
    assert radio.frequencia_atual == None
def test_desligar_radio_desligado(radio):
    radio.desligar()
    assert radio.desligar() == "O rádio já encontra-se desligado."
    assert radio.ligado == False
    assert radio.volume == None
    assert radio.estacao_atual == None
    assert radio.frequencia_atual == None

# Testes aplicados ao método AUMENTAR_VOLUME
def test_aumentar_volume_com_radio_desligado(radio):
    resposta = radio.aumentar_volume()
    assert radio.ligado == False
    assert resposta == "Só é possível aumentar o volume com o rádio ligado."
def test_aumentar_volume_do_radio_com_argumento(radio):
    radio.ligar()
    resposta1 = radio.aumentar_volume(50)
    assert resposta1 == "O volume do rádio foi aumentado para 50"
    assert radio.volume == 50
    resposta2 = radio.aumentar_volume(25)
    assert resposta2 == "O volume do rádio foi aumentado para 75"
    assert radio.volume == 75
def test_aumentar_volume_do_radio_sem_argumento(radio):
    radio.ligar()
    resposta1 = radio.aumentar_volume()
    assert resposta1 == "O volume do rádio foi aumentado para 1"
    assert radio.volume == 1
    resposta2 = radio.aumentar_volume()
    assert resposta2 == "O volume do rádio foi aumentado para 2"
    assert radio.volume == 2
def test_ultrapassar_volume_maximo_do_radio_sem_sucesso(radio):
    radio.ligar()
    radio.aumentar_volume(100)
    resposta = radio.aumentar_volume()
    assert resposta == "Não é possível ir além do volume 100!"
    assert radio.volume == 100
    
# Testes aplicados ao método DIMINUIR_VOLUME
def test_diminuir_volume_com_radio_desligado(radio):
    resposta = radio.diminuir_volume()
    assert radio.ligado == False
    assert resposta == "Só é possível diminuir o volume com o rádio ligado."
def test_diminuir_volume_do_radio_com_argumento(radio):
    radio.ligar()
    radio.aumentar_volume(100)
    resposta1 = radio.diminuir_volume(50)
    assert resposta1 == "O volume do rádio foi diminuído para 50"
    assert radio.volume == 50
    resposta2 = radio.diminuir_volume(25)
    assert resposta2 == "O volume do rádio foi diminuído para 25"
    assert radio.volume == 25
def test_diminuir_volume_do_radio_sem_argumento(radio):
    radio.ligar()
    radio.aumentar_volume(100)
    resposta1 = radio.diminuir_volume()
    assert resposta1 == "O volume do rádio foi diminuído para 99"
    assert radio.volume == 99
    resposta2 = radio.diminuir_volume()
    assert resposta2 == "O volume do rádio foi diminuído para 98"
    assert radio.volume == 98
def test_ultrapassar_volume_minimo_do_radio_sem_sucesso(radio):
    radio.ligar()
    radio.aumentar_volume(100)
    radio.diminuir_volume(100)
    resposta = radio.diminuir_volume()
    assert resposta == "Não é possível ir mais baixo que o volume 0!"
    assert radio.volume == 0

# Testes aplicados ao método MUDAR_FREQUENCIA
def test_mudar_frequencia_com_radio_desligado(radio):
    resposta = radio.mudar_frequencia()
    assert radio.ligado == False
    assert resposta == "O rádio precisa estar ligado para mudar de frequência."        
def test_mudar_frequencia_com_antena_desabilitada(radio):
    radio.ligar()
    resposta = radio.mudar_frequencia()
    assert radio.ligado == True
    assert radio.antena_habilitada == False
    assert resposta == "A antena deve ser habilitada para trocar de frequência!"
def test_mudar_frequencia_automaticamente(radio):
    radio.ligar()
    radio.antena_habilitada = True
    resposta1 = radio.mudar_frequencia()
    assert resposta1 == "Troca automática. Próxima estação: 89.5 - Cocais"
    assert radio.estacao_atual == "Cocais"
    assert radio.frequencia_atual == 89.5
    resposta2 = radio.mudar_frequencia()
    assert resposta2 == "Troca automática. Próxima estação: 91.5 - Mix"
    assert radio.estacao_atual == "Mix"
    assert radio.frequencia_atual == 91.5
    resposta3 = radio.mudar_frequencia()
    assert resposta3 == "Troca automática. Próxima estação: 94.1 - Boa"
    assert radio.estacao_atual == "Boa"
    assert radio.frequencia_atual == 94.1
    resposta4 = radio.mudar_frequencia()
    assert resposta4 == "Troca automática. Próxima estação: 99.1 - Clube"
    assert radio.estacao_atual == "Clube"
    assert radio.frequencia_atual == 99.1
    resposta5 = radio.mudar_frequencia()
    assert resposta5 == "Troca automática. Próxima estação: 89.5 - Cocais"
    assert radio.estacao_atual == "Cocais"
    assert radio.frequencia_atual == 89.5
    
def test_mudar_frequencia_manualmente_com_resultado(radio):
    radio.ligar()
    radio.antena_habilitada = True
    resposta1 = radio.mudar_frequencia(99.1)
    assert resposta1 == "Troca manual para 99.1, você está ouvindo a estação Clube"
    assert radio.estacao_atual == "Clube"
    assert radio.frequencia_atual == 99.1
    resposta2 = radio.mudar_frequencia(94.1)
    assert resposta2 == "Troca manual para 94.1, você está ouvindo a estação Boa"
    assert radio.estacao_atual == "Boa"
    assert radio.frequencia_atual == 94.1
def test_mudar_frequencia_manualmente_sem_resultado(radio):
    radio.ligar()
    radio.antena_habilitada = True
    resposta = radio.mudar_frequencia(78.4)
    assert resposta == "Estação inexistente."
    assert radio.estacao_atual == None
    assert radio.frequencia_atual == 78.4
