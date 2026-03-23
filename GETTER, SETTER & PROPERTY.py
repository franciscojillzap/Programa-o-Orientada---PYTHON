#Declaração de Classe
class Cofre_Eletronico:
    #Método Construtor
    def __init__(self, senha, codigo_mestre, estado="fechado", tentativas=3):
        self.__senha = senha
        self.__codigo_mestre = codigo_mestre
        self.__estado = estado
        self.__tentativas = tentativas
        self.__historico = []


    #GETTER - Lê um atributo
    def get_estado(self):
        return self.__estado #cofre1.get_estado()
    
    #SETTER - Modifica um atributo
    def set_estado(self, novo_estado):
        if novo_estado in ["aberto", "fechado", "bloqueado"]:
            self.__estado = novo_estado #cofre.set_estado("aberto")
            
    #@PROPERTY - Forma moderna de utilizar GET/SET
    @property #para GETTER
    def estado(self):
        return self.__estado #cofre1.estado

    @estado.setter #para SETTER
    def estado(self, novo_estado):
        if novo_estado in ["aberto", "fechado", "bloqueado"]:
            self.__estado = novo_estado #cofre1.estado = "fechado"
