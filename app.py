from flask import Flask, render_template, session, jsonify, request
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

boggle_game = Boggle()

@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    session['score'] = 0  # Initialize the score for a new game
    return render_template('index.html', board=board)

@app.route('/check-word')
def check_word():
    word = request.args.get('word')
    board = session['board']
    result = boggle_game.check_valid_word(board, word)

    if result == "ok":
        session['score'] += len(word)  # Increment the score based on the word length
        print(f"Word: {word}, Score: {session['score']}")  # Debug: log score updates

    return jsonify({'result': result, 'score': session['score']})  # Return the updated score


@app.route('/post-score', methods=['POST'])
def post_score():
    score = request.json.get("score", 0)
    highscore = session.get('highscore', 0)
    times_played = session.get('times_played', 0)

    session['times_played'] = times_played + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)

if __name__ == "__main__":
    app.run(debug=True)
