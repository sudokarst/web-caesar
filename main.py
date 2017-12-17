from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rotate-by">Rotate by:<label>
            <input id="rotate-by" type="text" name="rot" value="{rot}">
            <textarea name="text">{text}</textarea>
            <input type="submit" value="submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    rot = 0
    text = "Your plaintext secret here . . ."
    return form.format(**locals())

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    text = rotate_string(text, rot)
    rot = 26 - (rot % 26)
    return form.format(**locals())


app.run()