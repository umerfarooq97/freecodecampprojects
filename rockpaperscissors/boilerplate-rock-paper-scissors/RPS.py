import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.transition_matrix = defaultdict(lambda: defaultdict(int))

    def update(self, prev_move, move):
        self.transition_matrix[prev_move][move] += 1

    def predict(self, prev_move):
        if not self.transition_matrix[prev_move]:
            return random.choice(["R", "P", "S"])
        else:
            move_probs = self.transition_matrix[prev_move]
            total_moves = sum(move_probs.values())
            move_probs = {move: prob / total_moves for move, prob in move_probs.items()}
            return max(move_probs, key=move_probs.get)

def player(prev_play, opponent_history=[]):
    if not prev_play:
        return random.choice(["R", "P", "S"])

    opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    markov_chain = MarkovChain()
    for i in range(1, len(opponent_history)):
        markov_chain.update(opponent_history[i-1], opponent_history[i])

    predicted_move = markov_chain.predict(prev_play)
    if predicted_move == "R":
        return "P"
    elif predicted_move == "P":
        return "S"
    else:
        return "R"