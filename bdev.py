from flask import *
import os

app = Flask(__name__)
application = app
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/games')
def games():
    return render_template('games.html')
@app.route('/updates')
def contact():
    return render_template('contact.html')



app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# deployed to railway and render