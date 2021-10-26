## jogo matematico, pergunte a dificuldade, gere as contas
## Pergunte sempre se o jogador pretende continuar e some os pontos


## Import do modulo de random para colocar nas contas e para selecionar as operações
import random


print("olá jogador!! Vamos jogar um jogo?!")
print("O jogo funciona assim, você vai escolher a dificuldade\n"
      "e eu vou te dar uma missão, se você acertar, você ganha 2 pontos.\n"
      "Caso você erre, você perderá 3 pontos, você vence quando chega a um total de 12 pontos")
dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                        '[1] Para fácil\n'
                        '[2] Para Intermediário\n'
                        '[3] Para Dificil\n'
                        'Digite aqui: '))
score = 0
contador = 0
while dificuldade not in (1,2,3):
    print('Digite uma das opções')
    dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                            '[1] Para fácil\n'
                            '[2] Para Intermediário\n'
                            '[3] Para Dificil\n'
                            'Digite aqui: '))

while dificuldade in (1,2,3,4):
        ## Dificuldade fácil
    if dificuldade == 1:
        ## Para dificuldade fácil, apenas contas simples de adição e subtração
        oper = random.randint(0,1)
        if oper == 0:
            ##Operação de adição
            x = random.randint(0,999)
            y = random.randint(0,999)
            z = x + y
            a = int(input(f'Temos a conta: {x} + {y}, Qual é o Resultado dela? :: '))
            if a == z:
                score += 2
                print(f"Parabéns, você acertou!! {x} + {y} = {z}.")
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f"Que pena, você errou! O Resultado de {x} + {y} = {z}, e não {a}")
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
        if oper == 1:
            ##Operação de Subtração
            x = random.randint(0, 999)
            y = random.randint(0, 999)
            z = x - y
            a = int(input(f'Temos a conta: {x} - {y}, Qual é o Resultado dela? :: '))
            if a == z:
                score += 2
                print(f"Parabéns, você acertou!! {x} - {y} = {z}.")
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f"Que pena, você errou! O Resultado de {x} - {y} = {z}, e não {a}")
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))

        ## Dificuldade Intermediária
    if dificuldade == 2:
        ## Para dificuldade intermediário , contas de multiplicação e divisão
        oper = random.randint(0, 1)
        if oper == 0:
        ##Operação de multiplicação
            x = random.randint(0, 999)
            y = random.randint(0, 999)
            z = x * y
            a = int(input(f'Temos a conta: {x} * {y}, Qual é o Resultado dela? :: '))
            if a == z:
                score += 2
                print(f"Parabéns, você acertou!! {x} * {y} = {z}.")
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f"Que pena, você errou! O Resultado de {x} * {y} = {z}, e não {a}")
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))

        if oper == 1:
        ##Operação de Divisão
            x = random.randint(0, 999)
            y = random.randint(0, 999)
            z = x / y
            a = int(input(f'Temos a conta: {x} / {y}, Qual é o Resultado dela? :: '))
            if a == z:
                score += 2
                print(f"Parabéns, você acertou!! {x} / {y} = {z}.")
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f"Que pena, você errou! O Resultado de {x} / {y} = {z}, e não {a}")
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
    ## dificuldade Dificil
    if dificuldade ==3:
        ## Contas com todas operações e parenteses para prioridade
        oper = random.randint(0, 4)
        ## criar vários cenários para as contas
        if oper == 0:
            x = random.randint(0, 999)
            x2 = random.randint(0, 999)
            x3 = random.randint(0, 999)
            x4 = random.randint(0, 999)
            x5 = random.randint(0, 999)
            z = (x + x2) * (x4 - x5) + x3
            a = int(input(f'qual é o resultado dessa conta ({x} + {x2}) * ({x4} - {x5}) + {x3} :: '))
            if a == z:
                print(f'Parabéns, o Resultado é {z}, Você acertou!!')
                score += 2
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f'O Resultado era {z} , e não {a}. Tente novamente!')
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))

        if oper == 1:
            x = random.randint(0, 999)
            x2 = random.randint(0, 999)
            x3 = random.randint(0, 999)
            x4 = random.randint(0, 999)
            x5 = random.randint(0, 999)
            z = (x - x2) / (x4 - x5) + x3
            a = int(input(f'qual é o resultado dessa conta ({x} - {x2}) / ({x4} - {x5}) + {x3} :: '))
            if a == z:
                print(f'Parabéns, o Resultado é {z}, Você acertou!!')
                score += 2
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f'O Resultado era {z} , e não {a}. Tente novamente!')
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))

        if oper == 2:
            x = random.randint(0, 999)
            x2 = random.randint(0, 999)
            x3 = random.randint(0, 999)
            x4 = random.randint(0, 999)
            x5 = random.randint(0, 999)
            z = (x * x2) * (x4 + x5) / x3
            a = int(input(f'qual é o resultado dessa conta ({x} * {x2}) * ({x4} + {x5}) / {x3} :: '))
            if a == z:
                print(f'Parabéns, o Resultado é {z}, Você acertou!!')
                score += 2
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f'O Resultado era {z} , e não {a}. Tente novamente!')
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))

        if oper == 3:
            x = random.randint(0, 999)
            x2 = random.randint(0, 999)
            x3 = random.randint(0, 999)
            x4 = random.randint(0, 999)
            x5 = random.randint(0, 999)
            z = (x / x2) * (x4 - x5) / x3
            a = int(input(f'qual é o resultado dessa conta ({x} / {x2}) * ({x4} - {x5}) / {x3} :: '))
            if a == z:
                print(f'Parabéns, o Resultado é {z}, Você acertou!!')
                score += 2
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f'O Resultado era {z} , e não {a}. Tente novamente!')
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))

        if oper == 4:
            x = random.randint(0, 999)
            x2 = random.randint(0, 999)
            x3 = random.randint(0, 999)
            x4 = random.randint(0, 999)
            x5 = random.randint(0, 999)
            z = (x * x2) - (x4 * x5) / x3
            a = int(input(f'qual é o resultado dessa conta ({x} * {x2}) - ({x4} * {x5}) / {x3} :: '))
            if a == z:
                print(f'Parabéns, o Resultado é {z}, Você acertou!!')
                score += 2
                if score > 10:
                    break
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
            else:
                print(f'O Resultado era {z} , e não {a}. Tente novamente!')
                score -= 3
                print(f'O seu score atual é: {score}')
                dificuldade = int(input('Digite o a Dificuldade que você deseja jogar: \n'
                                        '[1] Para fácil\n'
                                        '[2] Para Intermediário\n'
                                        '[3] Para Dificil\n'
                                        '[4] Para Parar\n'
                                        'Digite aqui: '))
    if dificuldade == 4:
        break

if score > 10:
    print('PARABÉNS JOGADOR')
    print(f'Você conseguiu em {contador} rodadas alcançar os {score} pontos')
else:
    print(f'Você parou de jogar com um total de {contador} rodadas e com {score}')


