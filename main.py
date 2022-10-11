from Board import Board


def main(board: Board) -> None:
    """Função principal.

    Args:
        board (Board): O objeto responsável pelo tabuleiro.
    """

    # Aplica o algoritmo de força bruta para "N" rainhas em um tabuleiro "NxN".
    has_solution: bool = board._brute_force_n_queens_on_board()
    # Imprime o tabuleiro com as rainhas (caso tenha solução) ou vazio (caso
    # não tenha solução.)
    print(*board.board, sep="\n")
    # Indica se uma solução foi encontrada ou não.
    print("Solução Encontrada!" if has_solution else "Sem solução!")


if __name__ == "__main__":
    main(
        # Cria um tabuleiro de tamanho "NxN", isto é, "sizexsize".
        Board(
            size=8 # Tamanho do tabuleiro (NxN). / Pode ser alterado, mas por padrão, "size = 8".
        )
    )
