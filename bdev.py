from flask import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/games')
def games():
    return render_template('games.html')
@app.route('/updates')
def contact():
    return render_template('contact.html')



app.run(debug=True)
