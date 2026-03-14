#Declaração de Classe
class Cofre_Eletronico:
    #Método Construtor
    def __init__(self, senha):
        self.senha = senha
        self.estado = "fechado"
        self.tentativas_restantes = 3

    #Muda o estado do cofre para ABERTO, se:
    #A senha for CORRETA
    #Caso a senha seja INCORRETA:
    #Reduz o número de tentativas disponíveis
    def abrir_cofre(self, senha):     
        if self.senha == senha:
            self.estado = "aberto"
            return "Cofre aberto com sucesso!"
        elif self.senha != senha:
            self.tentativas_restantes -= 1
            return "Senha incorreta"
        if self.tentativas_restantes == 0:
            return "Número de tentativas esgotado. Cofre bloqueado."   

    #Muda o estado do cofre para FECHADO, caso:
    #Seu estado atual seja ABERTO
    def fechar_cofre(self):
        if self.estado == "aberto":
            self.estado = "fechado"
            return "Cofre fechado."
        else:
            return "O cofre já encontra-se fechado."

    #Reseta o número de tentativas para 3, apenas:
    #Se o cofre estiver ABERTO
    def resetar_tentativas(self):
        if self.estado == "aberto":
            self.tentativas_restantes = 3
            return "Tentativas resetadas para 3."
        else:
            return "Não é possível resetar as tentativas enquanto o cofre estiver fechado."

    #Permite mudar a senha do cofre, apenas se:
    #A senha antiga for CORRETA
    #O estado atual do cofre for ABERTO
    def trocar_senha(self, senha_antiga, senha_nova):
        pass
