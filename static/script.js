const cells = document.querySelectorAll(".cell");
const resetButton = document.getElementById("reset");

cells.forEach((cell) => {
  cell.addEventListener("click", handleMove);
});

resetButton.addEventListener("click", resetGame);

function handleMove(event) {
  const index = event.target.dataset.index;

  fetch("/move", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ move: parseInt(index) }),
  })
    .then((response) => response.json())
    .then((data) => {
      updateBoard(data.board);

      if (data.status === "HUMAN_WIN") alert("You win!");
      if (data.status === "AI_WIN") alert("AI wins!");
      if (data.status === "DRAW") alert("It's a draw!");
    });
}

function updateBoard(board) {
  cells.forEach((cell, index) => {
    cell.textContent = board[index] ? board[index] : "";
  });
}

function resetGame() {
  fetch("/reset", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => {
      updateBoard(data.board);
    });
}
