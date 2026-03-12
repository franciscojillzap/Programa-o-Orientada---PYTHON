#Declaração de Classe
class Card:
    cemiterio = []

    #Método Construtor
    def __init__(self, nome, tipo, ATK=0, DEF=0):
        self.nome = nome
        self.tipo = tipo
        self.ATK = ATK
        self.DEF = DEF
        

    #Retorna uma mensagem dependendo se o Card é MONSTRO, MAGIA ou ARMADILHA
    def invocar(self):
        if self.tipo == "monstro":
            return f"Eu invoco {self.nome}! Em Modo de Ataque!"
        elif self.tipo == "magia":
            return f"Eu ativo uma Carta Mágica! {self.nome}!"
        elif self.tipo == "armadilha":
            return f"Você ativou minha Carta Armadilha! {self.nome}!"
        else:
            return "Tipo de Card desconhecido."

    #Detalha informações sobre os Cards
    def detalhes(self):
        return f"Card: {self.nome}\nTipo: {self.tipo}\nATK: {self.ATK}\nDEF: {self.DEF}"

    #Altera os atributos de ATK e DEF dependendo se o Card for um Monstro
    def aumentar_atributos(self):
        if self.tipo == "monstro":
            self.ATK += 700
            self.DEF += 700
            return (self.ATK, self.DEF)
        else:
            return "Este Card não é um monstro!"

    #Realiza uma interação entre dois objetos (Cards) através do ATK de ambos
    def duelo(self, outro_monstro):
        if self.tipo == "monstro" and outro_monstro.tipo == "monstro":
            if self.ATK > outro_monstro.ATK:
                Card.cemiterio.append(outro_monstro)
                return f"{self.nome} com seu ataque superior enviou {outro_monstro.nome} para o cemitério!\n"
            elif self.ATK < outro_monstro.ATK:
                Card.cemiterio.append(self)
                return f"{self.nome} não resistiu ao ataque avassalador do {outro_monstro.nome}...\n"
            else:
                Card.cemiterio.append(self, outro_monstro)
                return f"Não houve vencedores. Ambos {self.nome} e {outro_monstro.nome} foram destruídos.\n"
        else:
            return "Um duelo só pode acontecer entre dois cards de monstro!"