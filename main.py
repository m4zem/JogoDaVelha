# Definir o tabu (tabuleiro) como lista de lista
tabu = [['X', '0', 'X'],
        ['0', 'X', '0'],
        ['X', '0', 'X']]

# Variável para rastrear o jogador atual
jogador_atual = "X"

#Variável para rastrear o estado do jogo
jogo_em_andamento = True

# Loop principal do jogo
while jogo_em_andamento:
    # Exibir o tabuleiro atual
    for linha in tabu:
        print("|".join(linha))
        print("-" * 9)

    # Obter a jogada do jogador
    linha = int(input(f"Jogador {jogador_atual}, escolha na linha (0, 1 ou 2): "))
    coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2)"))

    # Verificar se a jogada é válida
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabu[linha][coluna] != " ":
        print("Jogada inválida. Tente novamente.")
        continue

    # Faz a jogada no tabuleiro
    tabu[linha][coluna] = jogador_atual

    # Verifica se há um vencedor
    for linha in tabu:
        if all(posicao == jogador_atual for posicao in linha):
            print(f"Jogador {jogador_atual} venceu!")
            jogo_em_andamento = False
            break

    for coluna in range(3):
        if all(tabu[linha][coluna] == jogador_atual for linha in range(3)):
            print(f"Jogador {jogador_atual} venceu!")
            jogo_em_andamento = False
            break

    if all(tabu[i][i] == jogador_atual for i in range(3)) or all(tabu[i][2 - i] == jogador_atual for i in range(3)):
        print(f"Jogador {jogador_atual} venceu!")
        jogo_em_andamento = False

    # Verifica empate
    if all(posicao != " " for linha in tabu for posicao in linha):
        print("Empate!")
        jogo_em_andamento = False

    # Alterna o jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"