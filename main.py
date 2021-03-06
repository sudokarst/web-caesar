from flask import Flask, request, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

PLAINTEXT = "Your plaintext secret here . . ."
def is_integer(s):
    try:
        x = int(s)
    except ValueError:
        return False
    return True

@app.route("/")
def index():
    rot = 0
    rot_error = ''
    placeholder = PLAINTEXT
    return render_template("index.html", **locals())

@app.route("/", methods=['POST'])
def encrypt():
    placeholder = PLAINTEXT
    rot = request.form['rot']
    text = request.form['text']
    if is_integer(rot):
        rot = int(rot)
        if text.strip():
            text = rotate_string(text, rot)
            rot = (26 - (rot % 26) ) % 26
        else:
            text = ''
    else:
        rot_error = "must be an integer" 
    return render_template("index.html", **locals())


app.run()