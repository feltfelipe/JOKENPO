'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
print('\033[1;30m-*\033[m' * 17)
print('\033[1;33mJOKENPÔ - PEDRA, PAPEL E TESOURA\033[m')
print('\033[1;30m-*\033[m' * 17)
print('''Qual é a sua jogada?
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
opçoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
player = int(input('Escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-*' * 15)
print('O computador escolheu {}'.format(opçoes[computador]))
print('O jogador escolheu {}'.format(opçoes[player]))
print('-*' * 15)
if player == 0:
    if computador == 1:
        print('VOCÊ PERDEU!')
    elif computador == 2:
        print('VOCÊ GANHOU!!')
    elif computador == 0:
        print('EMPATE')
elif player == 1:
    if computador == 2:
        print('VOCÊ PERDEU!')
    elif computador == 0:
        print('VOCÊ GANHOU!')
    elif computador == 1:
        print('EMPATE')
elif player == 2:
    if computador == 0:
        print('VOCÊ PERDEU!')
    elif computador == 1:
        print('VOCÊ GANHOU')
    elif computador == 2:
        print('EMPATE')
else:
    print('Digite uma opção válida.')

