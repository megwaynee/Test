# Tic Tac Toe

This repository contains a simple Tic Tac Toe implementation in Python for the
console and an HTML/JavaScript frontend to play in the browser.

## Getting Started

Clone this repository and enter the project directory:

```bash
git clone <repository-url>
cd Test
```

From here you can run the game in the console or open it in a browser.

## Console Version
Run the Python script and enter moves as `row,col` (1-3):

```bash
python3 tic_tac_toe.py
```

You can exit at any time by typing `q`.

## Browser Version
Open `tic_tac_toe.html` in any modern browser to play using a graphical grid.
If your browser restricts local file access, you can start a quick web server:

```bash
python3 -m http.server
```

Then visit `http://localhost:8000/tic_tac_toe.html`. Click on a cell to place
your mark and press **Reset** to start a new game.
