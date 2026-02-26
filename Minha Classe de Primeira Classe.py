#Declaração de Classe
class Card:
    #Método Construtor
    def __init__(self, nome, tipo, ATK=0, DEF=0):
        #Atributos de Instância
        self.nome = nome
        self.tipo = tipo
        self.ATK = ATK
        self.DEF = DEF

    def invocar_ou_ativar(self):
        if self.tipo == "monstro":
            return f"Eu invoco {self.nome}! Em Modo de Ataque!"
        elif self.tipo == "magia":
            return f"Eu ativo uma Carta Mágica! {self.nome}!"
        elif self.tipo == "armadilha":
            return f"Você ativou minha Carta Armadilha! {self.nome}!"
    
    def detalhes(self):
        return f"\nCard: {self.nome}\nTipo: {self.tipo}\nATK: {self.ATK}\nDEF: {self.DEF}\n"
    
    def aumentar_atk(self):
        self.ATK += 700
        return f"Equipo Chifre de Unicórnio ao meu monstro! Ele ganha 700 pontos de ATK adicionais!\n\n{self.nome}\nATK: {self.ATK}\n"
    
    def aumentar_def(self):
        self.DEF += 500
        return f"Com Muralhas do Castelo, meu monstro ganha 500 pontos de DEF para resistir aos seus ataques!\n\n{self.nome}\nDEF: {self.DEF}\n"
    
    def duelo(self, outro_monstro):
        pass

#Declaração de Objetos
carta1 = Card("Mago Negro", "monstro", 2500, 2100)
print(carta1.invocar_ou_ativar())
print(carta1.detalhes())
print(carta1.aumentar_atk())
print(carta1.aumentar_def())

carta2 = Card("Pote da Ganância", "magia")
print(carta2.invocar_ou_ativar())

carta3 = Card("Cilindro Mágico", "armadilha")
print(carta3.invocar_ou_ativar())
