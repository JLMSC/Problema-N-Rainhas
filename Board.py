
from Queen import Queen


class Board:
    """Responsável pela representação do Tabuleiro."""

    def __init__(self, size: int = 8) -> None:
        """Cria um tabuleiro de tamanho: "size" por "size".

        Args:
            size (int, optional): O tamanho do tabuleiro (linha e coluna).
            Valor padrão: 8
        """

        # A variável responsável pelo tamanho do tabuleiro.
        self.size: int = size
        # O tabuleiro, de tamanho: "size" por "size".
        self.board: list[list[int | Queen]] = [
            [0 for _ in range(self.size)] 
            for _ in range(self.size)
        ]
        # As rainhas presentes no tabuleiro.
        self.queens_on_board: list[Queen] = []

    def is_inside_board(self, position: tuple[int, int]) -> bool:
        """Verifica se determinada posição está dentro do tabuleiro.

        Args:
            position (tuple[int, int]): Uma posição qualquer do tabuleiro.

        Returns:
            bool: Se a posição está dentro do tabuleiro.
        """
        (x, y) = position
        return 0 <= x < self.size and 0 <= y < self.size

    def add_queen_to_board(self, queen: Queen) -> None:
        """Adiciona uma rainha ao tabuleiro.

        Args:
            queen (Queen): A rainha a ser adicionada ao tabuleiro.
        """

        # Adiciona uma rainha ao tabuleiro caso a rainha não esteja no tabuleiro
        # e a quantidade de rainhas não seja maior que o "size" do tabuleiro.
        if queen not in self.queens_on_board and len(self.queens_on_board) <= self.size:
            # Verifica se a rainha está dentro do tabuleiro.
            if self.is_inside_board(queen.position):
                self.queens_on_board.append(queen)
                self.board[queen.y][queen.x] = queen
            else:
                raise ValueError(f"Posição: ({queen.position}) inválida ao adicionar uma rainha.")
    
    def remove_queen_from_board(self, queen: Queen) -> None:
        """Remove uma rainha do tabuleiro.

        Args:
            queen (Queen): A rainha a ser removida do tabuleiro.
        """

        # Remove uma rainha do tabuleiro caso a rainha exista no tabuleiro
        # e caso a quantia de rainhas no tabuleiro seja maior que 0.
        if queen in self.queens_on_board and len(self.queens_on_board) > 0:
            self.queens_on_board.remove(queen)
            self.board[queen.y][queen.x] = 0

    def _get_board_content(self, position: tuple[int, int]) -> int | Queen:
        """Retorna o conteúdo de determinada posição no tabuleiro.

        Args:
            position (tuple[int, int]): Uma posição qualquer do tabuleiro.

        Returns:
            int | Queen: Pode retorna um inteiro, representando nada ou uma rainha.
        """
        (x, y) = position
        return self.board[x][y]

    def _get_queens_under_attack(self) -> int:
        """Retorna a quantia de rainhas sobre ataque de outras rainhas no tabuleiro.

        Returns:
            int: A quantidade de rainhas sobre ataque.
        """

        # Os valores que, se somados a posição de uma rainha qualquer,
        # se moverá em determinada direção, sendo elas os ataques da
        # rainha, o mesmo do Xadrez.
        attacks_directions: list[tuple[int, int]] = [
            (-1, 0), # Esquerda.
            (1, 0), # Direita.
            (0, -1), # Cima.
            (0, 1), # Baixo.
            (-1, -1), # Diagonal Sup. Esq.
            (1, -1), # Diagonal Sup. Dir.
            (-1, 1), # Diagonal Inf. Esq.
            (1, 1) # Diagonal Inf. Dir.
        ]

        # As rainhas sobre ataque de outras rainhas.
        queens_under_attacked: list[Queen] = []

        # Itera sobre todas as rainhas no tabuleiro, verificando
        # se as mesmas estão atacando outras rainhas.
        for queen in self.queens_on_board:
            for direction in attacks_directions:
                # A posição da rainha.
                (x, y) = queen.position
                # A direção do ataque.
                (future_x, future_y) = direction
                # Verifica se a posição do ataque da rainha está dentro do tabuleiro.
                while self.is_inside_board((x, y)):
                    # Verifica se tem uma rainha na posição "X" e "Y".
                    position_content: int | Queen = self._get_board_content((y, x))
                    if isinstance(position_content, Queen):
                        # Verifica se a rainha já não foi contabilizada e se é diferente da rainha atual.
                        if position_content not in queens_under_attacked and position_content != queen:
                            queens_under_attacked.append(position_content)
                    y += future_y
                    x += future_x
        # Retorna a quantia de rainhas sobre ataque.
        return len(queens_under_attacked)

    def _brute_force_n_queens_on_board(self, column: int = 0) -> bool:
        """Coloca "N" rainhas no tabuleiro, sem que nenhuma rainha esteja sobre ataque.

        Args:
            column (int, optional): A coluna inicial, aquela na qual será adicionado
            a primeira rainha, depois a segunda e assim sucessivamente.
            Valor padrão: 0

        Returns:
            bool: Verdadeiro se for possível colocar "N" rainhas no tabuleiro, 
            Falso caso contrário.
        """

        # Verifica se adicionou "N" rainhas ao tabuleiro,
        # isto é, chegou (ou ultrapassou) o tamanho do tabuleiro.
        if column >= self.size:
            return True
        
        # Itera sobre todas as LINHAS da coluna atual.
        for row in range(self.size):
            
            # Adiciona uma rainha ao tabuleiro na posição "column" e "row",
            # com o objetivo de verificar se a rainha adicionada irá atacar
            # as demais rainhas ou estará livre de ataques.
            queen = Queen(position=(column, row))
            self.add_queen_to_board(queen)

            # Verifica se a rainha recém adicionada atacará, ou sofrerá,
            # ataques de outras rainhas.
            if not self._get_queens_under_attack():

                # Repete o processo na outra coluna, isto é: "column + 1".
                # Caso não seja possível adicionar rainhas na próxima coluna,
                # realiza-se o backtracking, ou seja, ele ajustará a posição
                # das rainhas anteriores até que seja possível adicionar novas rainhas.
                if (self._brute_force_n_queens_on_board(column + 1)):
                    return True

            # Caso a rainnha recém adiciona sofrer ataques de, ou atacar,
            # outras rainhas, ela é removida do tabuleiro e uma nova
            # posição é escolhida.
            self.remove_queen_from_board(queen)
        
        # Nenhuma solução foi encontrada.
        return False
