# codsoft_taskno.2
# Tic-Tac-Toe AI with Minimax

This project is a browser-based Tic-Tac-Toe game where you can play against an AI. The AI uses the Minimax algorithm to make the game unbeatable. It also has a simple user interface created with HTML, CSS, and JavaScript, while the game logic is powered by a Python backend using Flask.

## Project Structure

codsoft_taskno.2/ ├── app.py # Flask application for backend ├── requirements.txt # Python dependencies (Flask) ├── templates/ │ └── index.html # HTML interface for the game ├── static/ │ ├── style.css # CSS for the game's style │ └── script.js # JavaScript for client-side logic └── README.md # Project documentation


## Setup Instructions

1. Clone this repository

2. Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask server:
    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/` to play the game.

## How the Game Works

- You play as 'X' (Human), and the AI plays as 'O'.
- The AI uses the **Minimax algorithm** to determine the best move for each turn.
- The game continues until either the human wins, the AI wins, or it ends in a draw.
- You can reset the game at any time by clicking the "Reset Game" button.

## Technologies Used

- **Flask**: Backend framework for running the Python logic.
- **Minimax Algorithm**: Used by the AI to make the best move.
- **HTML/CSS/JavaScript**: Used for creating the interactive frontend.
