#Declaração de Classe
class Card:
    #Método Construtor
    def __init__(self, nome, tipo, ATK=0, DEF=0):
        self.nome = nome
        self.tipo = tipo
        self.ATK = ATK
        self.DEF = DEF

    #Retorna uma mensagem diferente dependendo se o Card é dos tipo MONSTRO, MAGIA ou ARMADILHA
    def invocar_ou_ativar(self):
        if self.tipo == "monstro":
            return f"Eu invoco {self.nome}! Em Modo de Ataque!"
        elif self.tipo == "magia":
            return f"Eu ativo uma Carta Mágica! {self.nome}!"
        elif self.tipo == "armadilha":
            return f"Você ativou minha Carta Armadilha! {self.nome}!"
        else:
            return "Tipo de carta desconhecido."

    #Detalha informações sobre os Cards
    def detalhes(self):
        return f"\nCard: {self.nome}\nTipo: {self.tipo}\nATK: {self.ATK}\nDEF: {self.DEF}\n"

    #Altera os atributos de ATK e DEF dependendo se o Card for um Monstro
    def aumentar_atributos(self):
        if self.tipo == "monstro":
            self.ATK += 700
            self.DEF += 700
            return f"Equipo Chifre de Unicórnio ao meu monstro! Ele ganha 700 pontos de ATK e DEF adicionais!\n\n{self.nome}\nATK: {self.ATK}\nDEF: {self.DEF}\n"
        else:
            return "Este Card não é um monstro!\n"

    #Realiza uma interação entre dois objetos (Cards) através do ATK de ambos
    def duelo(self, outro_monstro):
        if self.tipo == "monstro" and outro_monstro.tipo == "monstro":
            if self.ATK > outro_monstro.ATK:
                return f"{self.nome} com seu ataque superior enviou {outro_monstro.nome} para o cemitério!\n"
            elif self.ATK < outro_monstro.ATK:
                return f"{self.nome} não resistiu ao ataque avassalador do {outro_monstro.nome}...\n"
            else:
                return f"Não houve vencedores. Ambos {self.nome} e {outro_monstro.nome} foram destruídos.\n"
        else:
            return "Um duelo só pode acontecer entre dois cards de monstro!\n"

#Declaração de Objetos
carta1 = Card("Mago Negro", "monstro", 2500, 2100)
print(carta1.invocar_ou_ativar())
print(carta1.detalhes())

carta2 = Card("Dragão Branco de Olhos Azuis", "monstro", 3000, 2500)
print(carta2.invocar_ou_ativar())
print(carta2.detalhes())

print(carta1.duelo(carta2))
print(carta1.aumentar_atributos())
print(carta1.duelo(carta2))

carta3 = Card("Pote da Ganância", "magia")
print(carta3.invocar_ou_ativar())
print(carta3.aumentar_atributos())

carta4 = Card("Cilindro Mágico", "armadilha")
print(carta4.invocar_ou_ativar())
print(carta4.duelo(carta1))

