#Declaração de Classe
class card:
    #Método Construtor
    def __init__(self, nome, tipo):
        #Atributos de Instância
        self.nome = nome
        self.tipo = tipo

    def invocar_ou_ativar(self):
        if self.tipo == "monstro":
            return f"Eu invoco {self.nome}! Em Modo de Ataque!"
        elif self.tipo == "magia":
            return f"Eu ativo uma Carta Mágica! {self.nome}!"
        elif self.tipo == "armadilha":
            return f"Você ativou minha Carta Armadilha! {self.nome}!"

#Declaração de Objetos
carta1 = card("Mago Negro", "monstro")
print(carta1.invocar_ou_ativar())

carta2 = card("Pote da Ganância", "magia")
print(carta2.invocar_ou_ativar())

carta3 = card("Cilindro Mágico", "armadilha")
print(carta3.invocar_ou_ativar())
