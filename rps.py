import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, opponent_last_move):
        pass


class RandomPlayer(Player):
    def move(self):
        index = random.randint(0, 2)  # Selects random moves from the move list
        return moves[index]


# Remembers move opponent played last round, and plays that move next round
class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.opponent_last_move = None

    def move(self):
        if self.opponent_last_move is None:
            return Player.move(self)
        return self.opponent_last_move

    def learn(self, opponent_last_move):
        self.opponent_last_move = opponent_last_move


# remembers moves played in last round, and cycles through the different moves
class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.cycle = 0

    def move(self):
        if self.cycle == 'rock':
            move = moves[0]
            self.cycle = self.cycle + 1
        elif self.cycle == 'paper':
            move = moves[1]
            self.cycle = self.cycle + 1
        else:
            move = moves[2]
            self.cycle = self.cycle + 1
        return move


# asks the user what move(input) to make
class HumanPlayer(Player):
    def move(self):
        index = input('Choose: Rock, Paper, Scissors?  ').lower()
        while index not in moves:
            print('Invalid input! Choose again!')
            index = input('Choose: Rock, Paper, Scissors?  ').lower()
        return index


class Game:
    def __init__(self, p2):
        self.FirstPlayer = HumanPlayer()
        self.SecondPlayer = RandomPlayer()

    def play_game(self):
        print("\nLet's play Rock, Paper, Scissors!")
        for round in range(5):
            print(f"\nRound {round}:")
            self.play_round()
        if self.FirstPlayer.score > self.SecondPlayer.score:
            print('Player 1 is the WINNER!')
        elif self.FirstPlayer.score < self.SecondPlayer.score:
            print('Player 2 is the WINNER!')
        else:
            print('No one won, it\'s a tie!')
        print(f"Final score is {self.FirstPlayer.score} to {self.SecondPlayer.score}")

    # Plays a single round if user chose to
    def play_single(self):
        print("\nRock Paper Scissors!")
        for round in range(1, 2):
            print(f"Round {round} of {round}:")
            self.play_round()
        if self.FirstPlayer.score > self.SecondPlayer.score:
            print('You won!')
        elif self.FirstPlayer.score < self.SecondPlayer.score:
            print('Computer won!')
        else:
            print('It\'s a tie!')
        print(f"Final score is {self.FirstPlayer.score} to {self.SecondPlayer.score}")

    def play_round(self):
        move1 = self.FirstPlayer.move()
        move2 = self.SecondPlayer.move()
        Game.play(move1, move2)
        self.FirstPlayer.learn(move2)  # stores opponent move
        self.SecondPlayer.learn(move1)  # stores opponent move

    def play(self, move1, move2):
        print(f"You played {move1} and opponent played {move2}")

        if beats(move1, move2):
            print("--- PLAYER ONE WINS ---")
            self.FirstPlayer.score += 1
            print(f"[The score is {self.FirstPlayer.score} to {self.SecondPlayer.score}]\n")
            return 1
        elif beats(move2, move1):
            print("--- PLAYER TWO WINS ---")
            self.SecondPlayer.score += 1
            print(f"[The score is {self.FirstPlayer.score} to {self.SecondPlayer.score}]\n")
            return 2
        else:
            print("[ It's A TIE ]")
            print(f"[The score is {self.FirstPlayer.score} to {self.SecondPlayer.score}]\n")
            return 0


def beats(one, two):
    if one == 'rock' and two == 'scissors':
        return True
    elif one == 'scissors' and two == 'paper':
        return True
    elif one == 'paper' and two == 'rock':
        return True
    return False


if __name__ == '__main__':
    choice = [Player(), RandomPlayer()]
    mode = input('Select the Rock, Paper, Scissors game mode: \n' +
                 '[1] Rocks, [2] Random: ')

    # when a choice is not made, random mode will be selected
    while mode != 1 or mode != 2:
        mode = random.choice(choice)
        break
    if mode == '1':
        mode = Player()
    elif mode == '2':
        mode = RandomPlayer()

    rounds = input('\nChoose:\n\n[1] Single game or\n'
                   '[2] Full game (5 rounds): ')
    Game = Game(mode)
    while True:
        if rounds == '1':
            Game.play_single()
            break
        elif rounds == '2':
            Game.play_game()
            break
        else:
            print('Invalid choice!\n')
            rounds = input('Choose 1 or 2: ')
