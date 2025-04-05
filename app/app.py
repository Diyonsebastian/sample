from flask import Flask  # Corrected import statement

app = Flask(__name__)  # Corrected capitalization

@app.route('/')
def index():
    return "Hello, from the creator!"

if __name__ == '__main__':  # Corrected if condition
    app.run()