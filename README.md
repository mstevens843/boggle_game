# Boggle Game

## Overview

This is a Boggle game built using Python and Flask for the backend, and JavaScript (with jQuery and Axios) for the frontend. The game generates a 5x5 board of letters, allowing players to submit words by finding words in adjacent letters horizontally, vertically, or diagonally patterns. The user must find as many valid words as possible before the timer runs out.

## Features

- **Randomly Generated Board**: Each game generates a random 5x5 board of letters.
- **Word Validation**: Words are validated to ensure they are present in the dictionary and can be formed by connecting adjacent letters on the board.
- **Score Tracking**: The length of valid words is added to the player’s score.
- **High Score & Number of Plays**: The game tracks the highest score and the number of plays per session.
- **Timer**: Players have 60 seconds to find as many words as possible.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: JavaScript, jQuery, Axios
- **Templating**: Jinja2 (Flask)
- **Session Management**: Flask session

## How to Play

1. Open the game in a browser.
2. A random 5x5 grid of letters will appear.
3. Timer will start, enter words by typing them into the input box and pressing "Enter".
4. Words must be formed by connecting
5. For each word you get, points are calculated by the number of letters in word. 
