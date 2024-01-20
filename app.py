from flask import Flask, render_template, request, jsonify, redirect, url_for
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get('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'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('lesson2.html')

@app.route('/lesson3')
def lesson3():
    return render_template('lesson3.html')

@app.route('/lesson4')
def lesson4():
    return render_template('lesson4.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.json['message']

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message['content']
    except Exception as e:
        reply = f"An error occurred: {str(e)}"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
