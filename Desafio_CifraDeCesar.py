print("Desafio - Cifra de Cesar")

senha = list(str(input("Informe a senha que deseja criptografar: ")))

while True:
    try:
        chave = int(input("Informe o valor da chave de cesar: "))
        break
    except ValueError:
        print("Erro: o valor da chave de cesar tem que ser um número inteiro!")
        continue

tupla = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
k = -1

for caractere in senha:
    k += 1
    for n in tupla:
        if caractere == n:
            key = chave + tupla.index(n)
            while key >= 26:
                key -= 26
            while key < 0:
                key += 26
            senha[k] = tupla[key]
        elif caractere == n.upper():
            key = chave + tupla.index(n)
            while key >= 26:
                key -= 26
            while key < 0:
                key += 26
            senha[k] = tupla[key].upper()

conversao_lista_str = ''.join(senha)
print(f'A senha criptografada por cifra de César é {conversao_lista_str}')
