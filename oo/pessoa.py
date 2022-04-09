class Pessoa:
    def __init__(self, nome=None, idade=100):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá, {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Ana')
    print(Pessoa.cumprimentar(p))
    #Pode ser reduzido para:
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Lucas'
    print(p.nome)
    print(p.idade)