# app.py
from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from model_utils import generate_text, text, char_to_index, index_to_char, SEQ_LENGTH, characters

# import random

app = Flask(__name__)

model = load_model('trained_model.h5')

# def sample(preds, temperature=1.0):
#     preds = np.asarray(preds).astype('float64')
#     preds = np.log(preds) / temperature
#     exp_preds = np.exp(preds)
#     preds = exp_preds / np.sum(exp_preds)
#     probas = np.random.multinomial(1, preds, 1)
#     return np.argmax(probas)

# def generate_text(length, temperature, text, char_to_index, index_to_char, SEQ_LENGTH):
#     start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
#     generated = ''
#     sentence = text[start_index: start_index + SEQ_LENGTH]
#     generated += sentence
#     for i in range(length):
#         x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
#         for t, char in enumerate(sentence):
#             x_predictions[0, t, char_to_index[char]] = 1

#         predictions = model.predict(x_predictions, verbose=0)[0]
#         next_index = sample(predictions, temperature)
#         next_character = index_to_char[next_index]

#         generated += next_character
#         sentence = sentence[1:] + next_character
#     return generated


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text_route():
    # length = int(request.form['length'])
    # temperature = float(request.form['temperature'])
    data = request.get_json()
    length = int(data['length'])
    temperature = float(data['temperature'])



    # Pass 'text' as a parameter to the generate_text function
    generated_text = generate_text(length, temperature)
    
    return {'generated_text': generated_text}
    

if __name__ == '__main__':
    app.run(debug=True)
