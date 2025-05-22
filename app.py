from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def shelf():
    return render_template('shelf.html')  # shelf.html should be in the templates folder

if __name__ == '__main__':
    app.run(debug=True)
