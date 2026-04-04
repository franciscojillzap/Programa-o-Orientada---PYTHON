#Uma biblioteca usada para manipulação avançada de sequências, combinações e ciclos.
from itertools import cycle

#Dicionário contendo as estações (valor) e suas respectivas frequência (chave)
estacoes = {89.5: "Cocais", 91.5: "Mix", 94.1: "Boa", 99.1: "Clube"}

class RadioFM:
    #Método Construtor
    def __init__(self, vol_max, estacoes):
        #Atributos
        self.__vol_min = 0
        self.__vol_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.__estacoes = estacoes
        self.__volume = None #getter
        self.__ligado = False #getter
        self.__estacao_atual = None #getter
        self.__frequencia_atual = None #getter
        self.__antena_habilitada = False #getter/setter
        #Atributo extra para realizar a troca automática presente no método MUDAR_FREQUENCIA()
        #cycle cria um iterador que repete elementos infinitamente
        self.__ciclo = cycle(self.__estacoes.keys())

    #Métodos GETTER/SETTER

    @property
    def volume(self):
        return self.__volume

    @property
    def ligado(self):
        return self.__ligado

    @property
    def estacao_atual(self):
        return self.__estacao_atual

    @property
    def frequencia_atual(self):
        return self.__frequencia_atual

    @property
    def antena_habilitada(self):
        return self.__antena_habilitada

    @antena_habilitada.setter
    def antena_habilitada(self, ativar):
        if isinstance(ativar, bool):
            self.__antena_habilitada = ativar
    
    #Métodos

    #Muda o estado do rádio para ligado (True), inicia com volume (0)
    #Se antena habilitada, começa na primeira estação e frequência correspondente 
    def ligar(self):
        self.__ligado = True
        self.__volume = self.__vol_min
    
        if self.__antena_habilitada == True:
            #Cria duas variáveis que recebem a CHAVE e o VALOR presentes no dicionário
            #O dicionário é convertido em uma lista contendo CHAVE e VALOR com list()
            #O índice [0] corresponde a primeira chave (89.5) e valor ("Cocais") da lista/dicionário
            frequencia, estacao = list(self.__estacoes.items())[0]

            self.__frequencia_atual = frequencia
            self.__estacao_atual = estacao
            
            return f"O rádio está ligado na estação: {self.__estacao_atual}"

        else:
            return "O rádio está ligado."

    #Muda o estado do rádio para desligado (False)
    def desligar(self):
        if self.__ligado == True:
            self.__ligado = False
            #Todos os atributos recebem None
            self.__volume = self.__frequencia_atual = self.__estacao_atual = None

            return "O rádio foi desligado."
        else:
            return "O rádio já encontra-se desligado."

    #AUMENTA o volume do rádio, apenas se o rádio estiver ligado
    #Há um atributo opcional criado para MODIFICAR o volume do rádio, por padrão recebe 1
    def aumentar_volume(self, vol=1):
        if self.__ligado == True:
            #Verifica se o volume ultrapassa o volume MÁXIMO permitido
            if self.__volume + vol > self.__vol_max:
                return f"Não é possível ir além do volume {self.__vol_max}!"
            else:
                #Define o valor mínimo (teto) que o volume pode atingir de acordo com o vol_max (100)
                self.__volume = min(self.__vol_max, self.__volume + vol)
                return f"O volume do rádio foi aumentado para {self.__volume}"
        else:
            return "Só é possível aumentar o volume com o rádio ligado."

    #DIMINUI o volume do rádio, apenas se o rádio estiver LIGADO
    #Há um atributo opcional criado para MODIFICAR o volume do rádio, por padrão recebe 1
    def diminuir_volume(self, vol=1):
        if self.__ligado == True:
            #Verifica se o volume ultrapassa o volume MÍNIMO permitido
            if self.__volume - vol < self.__vol_min:
                return f"Não é possível ir mais baixo que o volume {self.__vol_min}!"
            else:
                #Define o valor máximo (piso) que o volume pode atingir de acordo com o vol_min (0)
                self.__volume = max(self.__vol_min, self.__volume - vol)
                return f"O volume do rádio foi diminuído para {self.__volume}"
        else:
            return "Só é possível diminuir o volume com o rádio ligado."

    #Troca a frequência do rádio de forma MANUAL ou AUTOMÁTICA
    #Verifica se o rádio está LIGADO e a antena HABILITADA
    def mudar_frequencia(self, freq=0):
        if self.__ligado == True:
            if self.__antena_habilitada == True:
                #Se nenhum argumento for passado na chamada do método, ativa a função troca AUTOMÁTICA
                if freq == 0:
                    #next() retorna o próximo item (frequência) da sequência
                    self.__frequencia_atual = next(self.__ciclo)
                    self.__estacao_atual = self.__estacoes[self.__frequencia_atual]
                    return f"Troca automática. Próxima estação: {self.__frequencia_atual} - {self.__estacao_atual}"

                #Verifica se argumento passado na chamada da função se encontra no DICIONÁRIO das estações
                if freq in self.__estacoes:
                    self.__frequencia_atual = freq
                    self.__estacao_atual = self.__estacoes.get(freq)
                    return f"Troca manual para {self.__frequencia_atual}, você está ouvindo a estação {self.__estacao_atual}"
                else:
                    self.__frequencia_atual = freq
                    self.__estacao_atual = None
                    return "Estação inexistente."
            else:
                return "A antena deve ser habilitada para trocar de frequência!"
        else:
            return "O rádio precisa estar ligado para mudar de frequência."        


gaga = RadioFM(100, estacoes)
gaga.ligar()
gaga.antena_habilitada = True
print(gaga.mudar_frequencia(99.1))
print(gaga.mudar_frequencia(89.5))
print(gaga.mudar_frequencia(94.1))
print(gaga.mudar_frequencia(91.5))
print(gaga.mudar_frequencia(100.5))
print(gaga.estacao_atual)
print(gaga.frequencia_atual)








