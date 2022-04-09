class Pessoa:
    def cumprimentar(self):
        return f'Olá, {id(self)}'

if __name__ == '__main__':
    p = Pessoa
    print(Pessoa.cumprimentar(p))
    #Pode ser reduzido para:
    print(p.cumprimentar(p))