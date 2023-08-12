
class GameBoard:
    def __init__(self, players, num_lanes=4, num_rows=2):
        self.num_lanes = num_lanes
        self.num_rows = num_rows
        self.players = players
        self.board = {player: [[None] * num_rows for _ in range(num_lanes)]
                      for player in players}

    def place_creature(self, player, creature, lane, row):
        if lane < 0 or lane >= len(self.lanes):
            raise ValueError("Invalid lane index")
        if row < 0 or row >= 2:
            raise ValueError("Invalid row index")
        if player not in self.board:
            raise ValueError("Invalid Player")
        if self.board[player][lane][row]:
            raise ValueError(
                f"board space {player}, lane {lane}, row {row} "
                + f"is occupied by creature {self.board[player][lane][row]}.")
        self.lanes[player][lane][row] = creature
