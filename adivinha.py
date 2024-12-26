import random

# Menu inicial de apresentação do desafio
print("=" * 50)
print('Seja bem vindo ao desafio: "Adivinhe o número"!')
print('Acerte o número entre "1" e "100" para vencer.')
print("=" * 50)


# Seleção de dificuldade (as chances mudam de acordo com a dificuldade)
print("\nPara começar, selecione a dificuldade do desafio.")
print("Observe que: A dificuldade selecionado irá ditar o número de chances.")
escolha = input("\n(F) FÁCIL  -  (M) MÉDIO  -  (D) DIFÍCIL  ==== Escolha: ").lower()


if escolha      == 'f':
    chances = 15
elif escolha    == 'm':
    chances = 10
elif escolha    == 'd':
    chances = 5
else:
    print('ERRO! Selecione uma opção de dificuldade válida.')

print(f'Você terá {chances} chances para adivinhar o número. Boa sorte!')


# Randomização do número a ser adivinhado pelo jogador
numero = random.randint(1, 100)
# Variável que armazena o número de rodadas (chances utilizadas)
count  = 1


# Condicional para vencer, perder e validação
while count <= chances:
    print('')
    print("-" * 50)
    print(f'Rodada: {count}')
    print("-" * 50)
    chute = input('Digite seu chute: ')
    
    try:
        chute_int   = int(chute)
    except:
        print('Digite um número válido')
        continue
    
    
    if chute_int    == numero:
        print('Parabéns!! Você acertou.')
        break
    
    
    if chute_int  <= numero:
        print('Chute abaixo do número correto')
    else:
        print('Chute acima do número correto')
    
    
    if count == chances:
        print('Você perdeu!')
        break
    
    count +=1