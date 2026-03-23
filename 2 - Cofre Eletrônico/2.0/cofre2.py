#Importa a biblioteca DATETIME = (DATA/HORA)
from datetime import *
            
#Declaração de Classe
class Cofre_Eletronico:
    #Método Construtor
    def __init__(self, senha, codigo_mestre, estado="fechado", tentativas=3):
        self.__senha = senha
        self.__codigo_mestre = codigo_mestre
        self.__estado = estado
        self.__tentativas = tentativas
        self.__historico = []

    @property
    def senha(self):
        return self.__senha

    @property
    def codigo_mestre(self):
        return self.__codigo_mestre

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, novo_estado):
        novo_estado in ["aberto", "fechado", "bloqueado"]
        self.__estado = novo_estado

    @property
    def tentativas(self):
        return self.__tentativas

    @property
    def historico(self):
        return self.__historico
    
    #Faz o registro das tentativas de abertura do cofre
    def registrar_tentativa(self, sucesso):
        registro = {
            "Tentativa": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "Sucesso": sucesso
            }
        #O registro é salvo dentro do HISTÓRICO
        self.__historico.append(registro)
        
    #Muda o estado do cofre para ABERTO, se a senha for CORRETA
    #Caso a senha seja INCORRETA, reduz o número de tentativas disponíveis
    def abrir_cofre(self, senha):
        if self.__estado == "bloqueado":
            return "Cofre bloqueado! Use o código mestre!"
        if self.__senha == senha:
            self.__estado = "aberto"
            #É feito o registro da tentativa, retorna True se bem sucedido
            self.registrar_tentativa(True)
            return "Cofre aberto com sucesso!"
        else:
            self.__tentativas -= 1
            #É feito o registro da tentativa, retorna False se mal sucedido
            self.registrar_tentativa(False)
        if self.__tentativas == 0:
            self.__estado = "bloqueado"
            return "Número de tentativas esgotado. Cofre bloqueado."
        else:
            return  "Senha incorreta"
        

    #Muda o estado do cofre para FECHADO, caso seu estado atual seja ABERTO
    def fechar_cofre(self):
        if self.__estado == "aberto":
            self.__estado = "fechado"
            return "Cofre fechado."
        else:
            return "O cofre já encontra-se fechado."

    #Reseta o número de tentativas para 3, apenas se o cofre estiver ABERTO
    def resetar_tentativas(self):
        if self.__estado == "aberto":
            self.__tentativas = 3
            return "Tentativas resetadas para 3."
        else:
            return "Não é possível resetar as tentativas enquanto o cofre estiver fechado."

    #Altera a senha, se a senha antiga for CORRETA e o cofre estiver ABERTO
    def trocar_senha(self, senha_antiga, senha_nova):
        if self.__estado != "aberto":
            return "A senha só pode ser alterada se o cofre estiver aberto!"
        if len(senha_nova) < 6:
            return "A nova senha deve possuir pelo menos 6 caracteres!"

        #Verifica se a nova senha tem pelo menos 1 NÚMERO
        tem_numero = any(char.isdigit() for char in senha_nova)

        if not tem_numero:
            return "A nova senha deve conter pelo menos um número!"
        else:
            self.__senha = senha_nova
            return "Senha alterada com sucesso!"

    #Retorna a DATA, HORA e se a tentativa de abertura do cofre foi bem SUCEDIDA
    def exibir_historico(self):
        if not self.__historico:
            return "Nenhuma tentativa registrada até o momento."        
        for t in self.__historico:
            print(t)

    #Realiza o desbloqueio do cofre, se o código mestre estiver CORRETO
    def desbloquear_cofre(self, codigo):
        if self.__estado != "bloqueado":
            return f"O cofre não encontra-se bloqueado. Seu estado atual é {self.estado}!"
        if self.__codigo_mestre == codigo:
            self.__estado = "aberto"
            self.__tentativas = 3
            return "Cofre desbloqueado!"
        else:
            return "Código mestre incorreto."
