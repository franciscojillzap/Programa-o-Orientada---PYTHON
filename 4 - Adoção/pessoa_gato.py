# Classe Pessoa
class Pessoa:
    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__gato = None 

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def endereco(self):
        return self.__endereco

    @property
    def gato(self):
        return self.__gato

    def adotar(self, gato):
        self.__gato = gato
        gato.dono = self
        return f"{self.__nome} adotou {gato.nome}!"

    @property
    def gato_info(self):
        return "Não possui gatos" if self.__gato is None else self.__gato.nome

    def __str__(self):
        if self.__gato is None:
            gato_info = "Não possui gatos"
        else:
            gato_info = str(self.__gato)

        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Endereço: {self.__endereco}, Gato: {gato_info}"


# Classe Gato
class Gato:
    def __init__(self, peso, idade, cor, raca="Sem raça", nome="Sem nome"):
        self.__peso = peso
        self.__idade = idade
        self.__cor = cor
        self.__raca = raca
        self.__nome = nome
        self.__dono = None

    @property
    def peso(self):
        return self.__peso

    @property
    def idade(self):
        return self.__idade

    @property
    def cor(self):
        return self.__cor

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, novo_dono):
        self.__dono = novo_dono

    @property
    def dono_nome(self):
        return "Sem dono" if self.__dono is None else self.__dono.nome

    def __str__(self):
        if self.__dono is None:
            dono_nome = "Sem dono"
        else:
            dono_nome = self.__dono.nome

        return f"Nome: {self.__nome}, Raça: {self.__raca}, Peso: {self.__peso}, Idade: {self.__idade}, Cor: {self.__cor}, Dono: {dono_nome}"


# Criação de objetos para PESSOA & GATO
pessoa1 = Pessoa("Francisco José", 8226550394, "Teresina(PI)")
gato1 = Gato(1.5, 3, "Malhado", "Vira-lata", "Saori Kido")
gato2 = Gato(3, 5, "Laranja", "Siamês", "Kidoumaru")

# Pessoa sem gato
print(pessoa1)
print(gato1)

# Adota gato1
print(pessoa1.adotar(gato1))
print(pessoa1)

# Substitui pelo gato2
print(pessoa1.adotar(gato2))
print(pessoa1)

# Confirma substituição
print(pessoa1.gato)

