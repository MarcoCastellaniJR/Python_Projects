## criar uma base para Locadora de filmes

filmes = [" O 3 Mosqueteiros", "Toy Story", "Toy Story 2", "Toy Story 3","Toy Story 4"]
disponibilidade = [0,0,1,1,0]
## 1 Para Disponivel e 0 para Ja alugado

## Indice perguntando se é sobre locação ou cadastro de filmes
print('Boa tarde!!')
print('Vamos lá, o que você deseja fazer?')
q_ind = int(input('Para Realizar o cadastro de um filme, digite 1 \n'
                  'Para Realizar a locação de um filme, digite 2 \n'
                  'Opção Desejada: '))

while q_ind in (1, 2):
    if q_ind == 1:
        ## criando um cadastro para os filmes
        nome = str(input('Digite o nome do filme que você deseja cadastrar: '))
        filmes.append(nome)
        disponibilidade.append(1)
        q_ind = int(input('Para Realizar o cadastro de um filme, digite 1 \n'
                          'Para Realizar a locação de um filme, digite 2 \n'
                          'Opção Desejada: '))
    if q_ind == 2:
        # Pesquisa de existencia e disponibilidade do filme:
        q_filme = str(input('Digite o nome do filme que você deseja alugar :'))
        if q_filme in filmes:
            # confirmação da existencia do filme
            print(f'O filme {q_filme} está no nosso banco de dados.')
            q_disp = filmes.index(q_filme)
            #contagem da posição do filme para saber a posição da informação de disponibilidade
            if disponibilidade[q_disp] == 1:
                print(f'O filme {q_filme} está disponivel para locação.')
                desejo = str(input('Você deseja alugar o filme?'))
                if desejo in 'Ss':
                    disponibilidade[q_disp] = 0
                    print(f'Você acaba de alugar o filme {q_filme}')
            elif disponibilidade[q_disp] == 0:
                print(f'O filme {q_filme} não está disponivel para locação')

            else:
                print(f'Erro nos dados.')
    q_ind = int(input('Para Realizar o cadastro de um filme, digite 1 \n'
                          'Para Realizar a locação de um filme, digite 2 \n'
                          'Opção Desejada: '))


