from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()