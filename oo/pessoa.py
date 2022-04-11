class Pessoa:
    olhos = 2 #Atributo default ou de classe
    def __init__(self, *filhos, nome=None, idade=100):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {self.nome}'

if __name__ == '__main__':
    arthur = Pessoa(nome='Arthur')
    ana = Pessoa(arthur, nome='Ana')
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