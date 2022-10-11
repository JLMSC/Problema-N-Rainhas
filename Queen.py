class Queen:
    """Responsável pela representação da Rainha."""

    def __init__(self, position: tuple[int, int]) -> None:
        """Cria uma rainha nas posições "x" e "y" de um tabuleiro qualquer.

        Args:
            position (tuple[int, int]): A posição da rainha no tabuleiro.
        """
        (self.x, self.y) = position
        self.position = position

    def __repr__(self) -> str:
        """Representação 'str' da classe 'Queen'.
        Só para não ficar poluído quando for dar um 'print(board)'

        Returns:
            str: Retorna um simples 'Q'.
        """
        return "Q"
