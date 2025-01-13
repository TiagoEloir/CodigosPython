import random

print("\n------------------------------------------------------\n")
print("           Seja Bem Vindo ao Jogo de Cartas !           ")
print("\n------------------------------------------------------\n")

while True:
    try:
        jogadores = int(input("Informe a quantidade de jogadores\n"))
        break
    except ValueError:
        print("Erro: o numero de jogadores tem que ser um número inteiro!")
        continue

def gerarbaralho(qtd=1, joker='n', embaralhar='n'):
    baralho = [
        'k♥', 'j♥', 'q♥', '1♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥',
        'k♦', 'j♦', 'q♦', '1♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
        'k♣', 'j♣', 'q♣', '1♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣',
        'k♠', 'j♠', 'q♠', '1♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠',
    ]

    baralho = baralho * qtd

    if joker.lower() in ("sim", "s"):
        for n in range(qtd):
            baralho.append('Joker')
            baralho.append('Joker')

    if embaralhar.lower() in ("s", 'sim'):
        random.shuffle(baralho)

    return baralho

def mostrarbaralho(baralho):
    print(f"O baralho possui {len(baralho)} cartas !")
    print(f"As cartas no baralho são \n{baralho}")

def DarAsCartas(jogadores, baralho):
    divisao_cartas = len(baralho) // jogadores

    if len(baralho) % jogadores > 0:
        print(f"Infelizmente não foi possível dividir exatamente as cartas entre os jogadores, vão restar {len(baralho) % jogadores} cartas no baralho")

    contador = 0
    dicionario = {}

    for t in range(1, jogadores + 1):
        dicionario[f"Jogador {t}"] = baralho[contador:contador + divisao_cartas]
        contador += divisao_cartas

    return dicionario

print("Vamos começar o jogo !!!!")
while True:
    try:
        qtd = int(input("Voce quer jogar com quantos baralhos ?: "))
        break
    except ValueError:
        print("Erro: o numero de baralhos tem que ser um número inteiro!")
        continue
while qtd == 0:
    try:
        qtd = int(input("Voce quer jogar com quantos baralhos ?: "))
        break
    except ValueError:
        print("Erro: o numero de baralhos tem que ser um número maior que 0")
        continue

joker = input("Voce quer jogar com o Joker digite (s/n): ").strip().lower()
while joker not in ('s', 'n', 'sim', 'nao'):
    joker = input("Voce quer jogar com o Joker digite (s/n): ").strip().lower()

embaralhar = input("Voce quer embaralhar o baralho digite (s/n): ").strip().lower()
while embaralhar not in ('s', 'n', 'sim', 'nao'):
    embaralhar = input("Voce quer embaralhar o baralho digite (s/n): ").strip().lower()

baralho = gerarbaralho(qtd, joker, embaralhar)
print("O Baralho foi gerado, vamos dar as cartas aos jogadores !!!!!")
dicionario = DarAsCartas(jogadores, baralho)
print("Vamos exibir o baralho !!!")
mostrarbaralho(baralho)
print('Vamos mostrar as cartas dos jogadores !')

for jogador, cartas in dicionario.items():
    print(f"{jogador}: {cartas}")
