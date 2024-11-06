from flask import Flask, render_template, jsonify, request
import math

app = Flask(__name__)

# Constants for players
HUMAN = "X"
AI = "O"
EMPTY = None

# Initial empty board state
board = [EMPTY] * 9

# Function to check for a win
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[cell] == player for cell in combo) for combo in winning_combinations)

# Minimax algorithm without Alpha-Beta Pruning
def minimax(board, depth, is_maximizing):
    if check_win(board, AI):
        return 10 - depth
    if check_win(board, HUMAN):
        return depth - 10
    if all(cell is not None for cell in board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = None
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = None
                best_score = min(best_score, score)
        return best_score

# Function to get the best move for the AI
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] is None:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = None
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/move', methods=['POST'])
def make_move():
    global board
    data = request.json
    human_move = data.get("move")

    if board[human_move] is None:
        board[human_move] = HUMAN
        if check_win(board, HUMAN):
            return jsonify({"status": "HUMAN_WIN", "board": board})

        if all(cell is not None for cell in board):
            return jsonify({"status": "DRAW", "board": board})

        ai_move = get_best_move(board)
        board[ai_move] = AI
        if check_win(board, AI):
            return jsonify({"status": "AI_WIN", "board": board})

        if all(cell is not None for cell in board):
            return jsonify({"status": "DRAW", "board": board})

        return jsonify({"status": "CONTINUE", "board": board})
    
    return jsonify({"status": "INVALID_MOVE", "board": board})

@app.route('/reset', methods=['POST'])
def reset_game():
    global board
    board = [EMPTY] * 9
    return jsonify({"status": "RESET", "board": board})

if __name__ == "__main__":
    app.run(debug=True)
