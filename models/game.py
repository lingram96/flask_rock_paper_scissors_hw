class Game():

    def __init__(self, choice_1, choice_2):
        self.choice_1 = choice_1
        self.choice_2 = choice_2
       
    def play_game(self, choice_1, choice_2):
        if choice_1 == "rock" and choice_2 == "scissors":
            winner = choice_1
            return "Player 1 wins by playing " + winner
        if choice_1 == "scissors" and choice_2 == "rock":
            winner = choice_2
            return "Player 2 wins by playing " + winner
        if choice_1 == "paper" and choice_2 == "rock":
            winner = choice_1
            return "Player 1 wins by playing " + winner
        if choice_1 == "rock" and choice_2 == "paper":
            winner = choice_2
            return "Player 2 wins by playing " + winner
        if choice_1 == "paper" and choice_2 == "scissors":
            winner = choice_2
            return "Player 2 wins by playing " + winner
        if choice_1 == "scissors" and choice_2 == "paper":
            winner = choice_1
            return "Player 1 wins by playing " + winner
        if choice_1 == choice_2:
            winner = None
            return "It's a Draw. Play again!"
        
        
        

            
        



        
