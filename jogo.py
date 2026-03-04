import random

def nível_dificuldade():
    while True:
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil   (1–25,  8 tentativas)")
        print("2 - Normal   (1–50,  10 tentativas)")
        print("3 - Difícil (1–100,  12 tentativas)")
        print("0 - Sair do jogo")
        
        try:
            escolha = int(input("Digite o número da dificuldade: "))
            if escolha == 0:
                return None 
            if escolha in [1, 2, 3]:
                return escolha
            else:
                print("Opção inválida. Escolha 1, 2, 3 ou 0.")
        except ValueError:
            print("Por favor, digite apenas números.")


def jogar_rodada(nome, nivel, pontuacao_atual):
    if nivel == 1:
        max_num = 25
        max_tentativas = 8
        pontos_por_tentativa_restante = 15
    elif nivel == 2:
        max_num = 50
        max_tentativas = 10
        pontos_por_tentativa_restante = 25
    else: 
        max_num = 100
        max_tentativas = 12
        pontos_por_tentativa_restante = 40

    numero_secreto = random.randint(1, max_num)
    tentativas = 0
    
    print(f"\n{nome}, nível {nivel} selecionado!")
    print(f"Tente adivinhar o número entre 1 e {max_num}")
    print(f"Você tem {max_tentativas} tentativas.\n")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Seu palpite: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            tentativas_restantes = max_tentativas - tentativas
            pontos_ganhos = tentativas_restantes * pontos_por_tentativa_restante + 100
            pontuacao_atual += pontos_ganhos
            
            print(f"\nPARABÉNS, {nome}! Você acertou em {tentativas} tentativa(s)!")
            print(f"Você ganhou {pontos_ganhos} pontos nesta rodada!")
            break

        elif palpite < numero_secreto:
            print("Tente um número MAIOR.")
        else:
            print("Tente um número MENOR.")

        print(f"Tentativas restantes: {max_tentativas - tentativas}")

    else:
        print(f"\nQue pena, {nome}! As tentativas acabaram.")
        print(f"O número era {numero_secreto}.")
        pontos_ganhos = 0

    print(f"Pontuação atual: {pontuacao_atual} pontos")
    return pontuacao_atual

def main():
    print("=====================================")
    print("      JOGO DA ADIVINHAÇÃO       ")
    print("=====================================\n")

    nome = input("Digite seu nome: ").strip()

    while nome.isdigit() or not nome:
        print("Digite um nome válido, seu animal.(nõo pode ser so números)")
        nome = input("Digite seu nome ").strip()

    if not nome:
        nome = "Jogador"

    pontuacao_total = 0
    jogando = True

    while jogando:
        nivel = nível_dificuldade()
        
        if nivel is None:
            print("\n" + "="*40)
            print(f"Obrigado por jogar, {nome}!")
            print(f"Pontuação final acumulada: {pontuacao_total} pontos")
            print("="*40)
            break

        pontuacao_total = jogar_rodada(nome, nivel, pontuacao_total)

        while True:
            print("\nDeseja jogar novamente?")
            print("1 - Sim (escolher nível novamente)")
            print("0 - Não (encerrar jogo)")
            try:
                continuar = int(input("→ "))
                if continuar == 1:
                    break
                elif continuar == 0:
                    print("\n" + "="*40)
                    print(f"Até a próxima, {nome}!")
                    print(f"Pontuação final: {pontuacao_total} pontos")
                    print("="*40)
                    jogando = False
                    break
                else:
                    print("Digite 1 ou 0.")
            except ValueError:
                print("Digite apenas 1 ou 0.")

if __name__ == "__main__":
    main()