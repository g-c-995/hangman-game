from flask import Flask, render_template, request, jsonify
from hangman import HangmanGame

app = Flask(__name__)

game = HangmanGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.form.get('letter')
    if not letter or not letter.isalpha():
        return jsonify({'message': 'Please enter a valid letter!'}), 400
    
    game.make_guess(letter)
    return jsonify({'word': game.masked_word, 'guesses': game.guesses})

if __name__ == '__main__':
    app.run(debug=True)
