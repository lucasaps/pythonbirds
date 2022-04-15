class Pessoa:
    olhos = 2 #Atributo default ou de classe
    def __init__(self, *filhos, nome=None, idade=100):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos: {cls.olhos}'

    @staticmethod
    def metodo_estatico():
        return 42


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai = super().cumprimentar()
        return f'{cumprimentar_classe_pai}. Aperte a mão do senhor {self.nome}'

class Mutante(Pessoa):
    olhos = 4

if __name__ == '__main__':
    arthur = Homem(nome='Arthur')
    ana = Pessoa(arthur, nome='Ana')
    mutante = Mutante(nome='Metamorfo')
    print(ana.cumprimentar())
    print(arthur.cumprimentar())
    for filho in ana.filhos:
        print(filho.nome)
    ana.sobrenome='Lopes' # atributo criado em tempo de execução
    print(ana.sobrenome)
    print(ana.__dict__) # Não exibe atributos de classe
    print(arthur.__dict__)
    del ana.sobrenome
    print(Pessoa.olhos) # Pode ser acessado pela classe
    print(ana.olhos)
    print(Pessoa.metodo_estatico())
    print(arthur.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes())
    print(arthur.nome_e_atributos_de_classes())
    print(isinstance(ana,Pessoa))
    print(isinstance(ana, Homem))
    print(isinstance(arthur, Pessoa))
    print(isinstance(arthur, Homem))
    print(mutante.olhos)
    print(mutante.cumprimentar())