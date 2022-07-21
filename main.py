'''
Leia 2 números e mostre o maior e o menor.
(Valores inválidos: números menores que -99 e maiores que 99).
'''


class MaiorMenor:
    """
    Solicita ao usuario 2 numero (A e B) entre -99 a 99 para comparar qual é maior.

    """
    def __init__(self):
        self.a = -100
        self.b = -100

    def set_numeros(self):
        """
        Solicita ao usuario 2 numero (A e B) entre -99 a 99.
        """
        while self.a not in range(-99, 99):
            self.a = int(input('Insira um numero entre -99 a 99 para o valor de A: \n'))
            if self.a not in range(-99, 99):
                print('Valores inválidos: números menores que -99 e maiores que 99')

        while self.b not in range(-99, 99):
            self.b = int(input('Insira um numero entre -99 a 99 para o valor de B: \n'))
            if self.b not in range(-99, 99):
                print('Valores inválidos: números menores que -99 e maiores que 99')

    def comparar(self):
        """
        Compara qual dos numeros é maior.
        """
        if self.a > self.b:
            print('A maior que B')
        elif self.b > self.a:
            print('B é maior que A')
        else:
            print('A e B são iguais.')


n = MaiorMenor()
n.set_numeros()
n.comparar()
